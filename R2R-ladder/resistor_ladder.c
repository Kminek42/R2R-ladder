#include "resistor_ladder.h"
#include "stdlib.h"

double get_rand()
{
	return rand() / ((double)RAND_MAX);
}

double get_real_value( double value, double tolerance )
{
	return value + value * tolerance * 2.0 * (get_rand() - 0.5);
}

void init_ladder( ladder_t* ladder, double R, double R2, double GND_R, double tolerance )
{
	for ( int i = 0; i < RESOLUTION; i++ )
		ladder->R2[i] = get_real_value( R2, tolerance );

	for ( int i = 0; i < RESOLUTION - 1; i++ )
		ladder->R[i] = get_real_value( R, tolerance );

	ladder->GND_R = GND_R;
}

double get_voltage_at_bit( ladder_t* ladder, int bit )
{
	double Rr = get_resistance_right( ladder, bit );
	if ( Rr < 0.0 ) Rr = 0.0;
	else Rr = 1.0 / Rr;
	double resistance = 1.0 / (1.0 / get_resistance_left( ladder, bit ) + Rr);
	double U = resistance / (ladder->R2[bit] + resistance);
	return U;
}

double get_weight( ladder_t* ladder, int bit )
{
	double U = get_voltage_at_bit( ladder, bit );
	while ( bit < RESOLUTION - 1 )
	{
		U = U * (1.0 - ladder->R[bit] / get_resistance_right( ladder, bit ));
		bit++;
	}

	return U;
}

double get_resistance_right( ladder_t* ladder, int n )
{
	// returns resistance from msb resistor connected to GND, to point between n-th (from LSB) resistor connected to register and n-th resistor connected to GND
	if ( !RESOLUTION ) return -1;
	if ( n < 0 ) return -1;

	int i = RESOLUTION - 1;
	if ( i == n ) return -1;

	double resistance = ladder->R2[i] + ladder->R[i - 1];
	i--;

	while ( i > n )
	{
		resistance = 1.0 / (1.0 / ladder->R2[i] + 1.0 / resistance);
		resistance = ladder->R[i - 1] + resistance;
		i--;
	}

	return resistance;
}

double get_resistance_left( ladder_t* ladder, int n )
{
	// returns resistance from lsb resistor connected to GND, to point between n-th (from LSB) resistor connected to register and n-th resistor connected to GND
	if ( !RESOLUTION ) return -1;
	if ( n >= RESOLUTION ) return -1;

	int i = 0;
	if ( i == n ) return ladder->GND_R;

	double resistance = 1.0 / (1.0 / ladder->GND_R + 1.0 / ladder->R2[i]);
	resistance = ladder->R[i] + resistance;
	i++;

	while ( i < n )
	{
		resistance = 1.0 / (1.0 / ladder->R2[i] + 1.0 / resistance);
		resistance = ladder->R[i] + resistance;
		i++;
	}

	return resistance;
}
