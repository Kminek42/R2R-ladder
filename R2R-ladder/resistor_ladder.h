#pragma once
#define RESOLUTION 10

typedef struct
{
	double R2[RESOLUTION];
	double R[RESOLUTION - 1];
	double GND_R;
} ladder_t;

void init_ladder( ladder_t* ladder, double R, double R2, double GND_R, double tolerance );
double get_weight( ladder_t* ladder, int bit );
double get_resistance_right( ladder_t* ladder, int n );
double get_resistance_left( ladder_t* ladder, int n );
