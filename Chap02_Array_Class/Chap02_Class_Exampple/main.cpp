//#include "Car.h"
//#include "SportsCar.h"
#include <cstdio>
#include "Rectangle.h"
int main() {
	Rectangle r(10, 20);
	double perimeter = r.getPerimeter();
	std::cout << "Rectangle 1:" << std::endl;
	std::cout << "Area:" << r.getArea() << std::endl;
	std::cout << "Perimeter:" << perimeter << std::endl;
	std::cout << "is square" << std::boolalpha << r.isSquare() << std::endl;
}
/*//Car Ŭ���� ���
Car myCar(50,"K3",4);
Car yourCar(100, "K5", 3);
myCar.display();
yourCar.display();
myCar.whereAmI();
yourCar.whereAmI();
//SportsCar Ŭ���� ���
SportsCar scar;
scar.speedUp();*/

