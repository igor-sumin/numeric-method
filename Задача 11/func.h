#pragma once
#ifndef FUNC_H
#define FUNC_H

#include <iostream>
#include <math.h>
#include <vector>
using namespace std;
class func
{
private:
	double x, h, E;
	vector<double> v, parametrs;
public:
	func(double X, vector<double> V, double H, double e);
	vector<double> RunKut4(double X, vector<double> V, double H);
	vector<double> Function(double X, vector<double> V);
	vector<double> LocalErrorControl(vector<double> V1, vector<double> V0, double H, double X);
	double min(vector<double> Vector);
	double max(vector<double> Vector);
	void GetParamerts(double a);
	vector<double> minus(const vector<double>& A, const vector<double>& B);
	vector<double> plus(const vector<double>& A, const vector<double>& B);
	vector<double> multiply(const vector<double>& A, const double& b);
	vector<double> divide(const vector<double>& A, const double& b);

};
#endif
