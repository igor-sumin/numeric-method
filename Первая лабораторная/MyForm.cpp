#include "MyForm.h"
#include <iostream>
#include <cmath>
#include <vector>
#include <windows.h>

using namespace System;
using namespace System::Windows::Forms;
using namespace std;

[STAThread]
int Main()
{
	SetConsoleOutputCP(CP_UTF8);
	Application::EnableVisualStyles();
	Application::SetCompatibleTextRenderingDefault(false);

	Graph::MyForm form;
	Application::Run(%form);

	return 0;
}