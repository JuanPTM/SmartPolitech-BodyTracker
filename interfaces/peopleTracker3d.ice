/*
 *  Copyright (C) 2013 Pentalo Labs Developers
 *
 *
 *  Authors : Francisco Miguel Rivas Montero <franciscomiguel.rivas@pentalo.com>
 *            Roberto Calvo Palomino <rocapal@pentalo.com
 *            Jose María Cañas <jmplaza@pentalo.com>
 */

#ifndef PEOPLETRACKER_ICE
#define PEOPLETRACKER_ICE

module peopleTracker3dMod {  

	struct PlayerPos{
	     float x;
	     float y;
	     float z;
	}; 
	
	sequence<PlayerPos> Positions;
	
	struct PersonInfo{
		Positions pos;
		PlayerPos size; //volume
		bool predicted;
		long id;
	};

	sequence<PersonInfo> People;

	struct peopleData{
		People data;
	};

	interface peopletracker3d{

		idempotent peopleData getData();
		
	};
};
#endif 
