#include "resistor_ladder.h"
#include "stdio.h"
#include "time.h"

void main()
{
	srand( (unsigned int)time( 0 ) );
	ladder_t DAC1;
	init_ladder( &DAC1, 1000, 2000, 2000, 0.01 );

	for ( int i = 0; i < RESOLUTION; i++ )
	{
		double a = get_weight( &DAC1, i );
		printf( "%.8f, \n", a );
	}
}
