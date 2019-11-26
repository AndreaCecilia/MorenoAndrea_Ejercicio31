rta.png: c.py
	python c.py

dataI.dat : evolve.x
	./evolve.x > dataI.dat

dataE.dat : evolve.x
	./evolve.x > dataE

dataC.dat : evolve.x
	./evolve.x > dataC.dat

evolve.x : evolve.cpp
	c++ c.cpp -o evolve.x

clean:
	rm evolve.x *.dat