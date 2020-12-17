#include "func.h"

func::func(double X, vector<double> V, double H, double e)
{
	vector<double> sup(1);
	x = X;
	v = V;
	h = H;
	E = e;
	parametrs = sup;
}


vector<double> func::RunKut4(double X, vector<double> V, double H)
{
	int k = v.size();
	vector<double> k1(k), k2(k), k3(k), k4(k), res(k);
	k1 = Function(X, V);
	k2 = Function(X + H / 2, plus(V, multiply(k1, H / 2)));
	k3 = Function(X + H / 2, plus(V, multiply(k2, H / 2)));
	k4 = Function(X + H, plus(V, multiply(k3, H)));
	res = plus(V, multiply(plus(plus(k1, multiply(k2, 2)), plus(k4, multiply(k3, 2))), H / 6));
	return res;
}
vector<double> func::minus(const vector<double>& A, const vector<double>& B) {
	vector<double> res(A.size());
	if (A.size() != B.size()) {
		exception("no");
	}
	for (int i = 0; i < A.size(); i++)
	{
		res[i] = A[i] - B[i];
	}
	return res;
}

vector<double> func::plus(const vector<double>& A, const vector<double>& B) {
	vector<double> res(A.size());
	if (A.size() != B.size()) {
		exception("no");
	}
	for (int i = 0; i < A.size(); i++)
	{
		res[i] = A[i] + B[i];
	}
	return res;
}

vector<double> func::multiply(const vector<double>& A, const double& b) {
	vector<double> res(A.size());
	for (int i = 0; i < A.size(); i++)
	{
		res[i] = A[i] * b;
	}
	return res;
}
vector<double> func::divide(const vector<double>& A, const double& b) {
	vector<double> res(A.size());
	if (b == 0) {
		exception("no");
	}
	for (int i = 0; i < A.size(); i++)
	{
		res[i] = A[i] / b;
	}
	return res;
}



vector<double> func::LocalErrorControl(vector<double> V1, vector<double> V0, double H, double X)
{
	int power = 0;
	vector<double> S(v.size()), V(v.size());
	vector<double> res(v.size() + 2);
	V = RunKut4(X, V0, H / 2);    // Vn+1/2
	V = RunKut4(X + H / 2, V, H / 2);   //V - Vn+1 с двум€ крышечками (полученное с шагом h/2), V1 - Vn+1 вычисленное с шагом h
	S = divide(minus(V, V1), 15);
	//Ѕерем модуль погрешности
	for (int i = 0; i < v.size(); i++)
	{
		S[i] = fabs(S[i]);
	}
	//Ќаходим max S
	S[0] = max(S);

	if (S[0] < E / 32)
	{
		H = H * 2;
	}
	else
	{
		if (S[0] > E)
		{
			H = H / 2;
		}
	}

	//«аписывает численное решение двойного хода с половинным шагом
	for (int j = 0; j < v.size(); j++)
	{
		res[j] = V[j];
	}
	//«аписывает полученный шаг
	res[v.size()] = H;
	//«аписывает локальную погрешность
	res[v.size() + 1] = S[0];
	return res;
}


vector<double> func::Function(double X, vector<double> V)
{
	vector<double> res(V.size());
	res[0] = V[1];
	res[1] = (-parametrs[1] * V[1] - parametrs[0] * V[0]) / parametrs[2];
	res[1] = (-parametrs[1] * V[1] - parametrs[0] * V[0]) / parametrs[2];
	return res;
}


double func::max(vector<double> vector)
{
	double res = vector[0];
	for (int i = 1; i < v.size(); i++)
	{
		if (vector[i] > res)
			res = vector[i];
	}
	return res;
}


double func::min(vector<double> vector)
{
	double res = vector[0];
	for (int i = 1; i < v.size(); i++)
	{
		if (vector[i] < res)
			res = vector[i];
	}
	return res;
}


void func::GetParamerts(double a)
{
	parametrs[0] = a;

}


