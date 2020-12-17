#pragma once
#include <math.h>
#include <vector>
#include <iostream>
#include "func.h"

using namespace std;


namespace Graph {

	using namespace System;
	using namespace System::ComponentModel;
	using namespace System::Collections;
	using namespace System::Data;
	using namespace System::Windows::Forms;
	using namespace System::Drawing;
	using namespace ZedGraph;


	/// <summary>
	/// Summary for MyForm
	/// </summary>
	public ref class MyForm : public System::Windows::Forms::Form
	{
	public:
		MyForm(void)
		{
			InitializeComponent();
			DrawGraph();
			//
			//TODO: Add the constructor code here
			//
		}



	protected:
		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		~MyForm()
		{
			if (components)
			{
				delete components;
			}
		}
	private: ZedGraph::ZedGraphControl^ zedGraphControl1;
	protected:

	protected:

	private: System::Windows::Forms::Button^ butt_draw;
	private: System::Windows::Forms::DataGridView^ dataGridView1;



	private: System::Windows::Forms::Label^ label_e;
	private: System::Windows::Forms::TextBox^ textBox_e;
	private: System::Windows::Forms::Label^ label_u0;
	private: System::Windows::Forms::TextBox^ textBox_u0;
	private: System::Windows::Forms::Label^ label_x0;
	private: System::Windows::Forms::TextBox^ textBox_x0;










	private: System::Windows::Forms::TextBox^ textBox_kol_vo_shag;
	private: System::Windows::Forms::Label^ label_kol_vo_shagov;
	private: System::Windows::Forms::TextBox^ textBox_h;





	private: System::Windows::Forms::Label^ label_h;





	protected:
	private: System::ComponentModel::IContainer^ components;

	private:






	private: System::Windows::Forms::Label^ label_Xmax;
	private: System::Windows::Forms::TextBox^ textBox_Xmax;















	private: System::Windows::Forms::Label^ label1;
	private: System::Windows::Forms::Label^ label2;
	private: System::Windows::Forms::ComboBox^ comboBox2;
















	private: System::Windows::Forms::Label^ label6;

	private: System::Windows::Forms::Label^ label4;









	private: ZedGraph::ZedGraphControl^ zedGraphControl2;


	private: System::Windows::Forms::Label^ label3;
	private: System::Windows::Forms::Label^ label5;
	private: System::Windows::Forms::TextBox^ textBox1;
	private: System::Windows::Forms::PictureBox^ pictureBox1;
	private: System::Windows::Forms::DataGridViewTextBoxColumn^ i;
	private: System::Windows::Forms::DataGridViewTextBoxColumn^ idXi;
	private: System::Windows::Forms::DataGridViewTextBoxColumn^ idVi;
	private: System::Windows::Forms::DataGridViewTextBoxColumn^ V22;
	private: System::Windows::Forms::DataGridViewTextBoxColumn^ V2i;
	private: System::Windows::Forms::DataGridViewTextBoxColumn^ Column1;
	private: System::Windows::Forms::DataGridViewTextBoxColumn^ Vi2i;
	private: System::Windows::Forms::DataGridViewTextBoxColumn^ Column2;
	private: System::Windows::Forms::DataGridViewTextBoxColumn^ OLP;
	private: System::Windows::Forms::DataGridViewTextBoxColumn^ Hi;
	private: System::Windows::Forms::DataGridViewTextBoxColumn^ C1;
	private: System::Windows::Forms::DataGridViewTextBoxColumn^ C2;
	private: System::Windows::Forms::Label^ label7;
	private: System::Windows::Forms::TextBox^ textBox2;
	private: System::Windows::Forms::Label^ label8;
	private: System::Windows::Forms::Label^ label9;
	private: System::Windows::Forms::Label^ label10;
	private: System::Windows::Forms::Label^ label11;


















		   double e;

		   /// <summary>
		   /// Required designer variable.
		   /// </summary>


#pragma region Windows Form Designer generated code
		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		   void InitializeComponent(void)
		   {
			   this->components = (gcnew System::ComponentModel::Container());
			   System::ComponentModel::ComponentResourceManager^ resources = (gcnew System::ComponentModel::ComponentResourceManager(MyForm::typeid));
			   this->zedGraphControl1 = (gcnew ZedGraph::ZedGraphControl());
			   this->butt_draw = (gcnew System::Windows::Forms::Button());
			   this->dataGridView1 = (gcnew System::Windows::Forms::DataGridView());
			   this->i = (gcnew System::Windows::Forms::DataGridViewTextBoxColumn());
			   this->idXi = (gcnew System::Windows::Forms::DataGridViewTextBoxColumn());
			   this->idVi = (gcnew System::Windows::Forms::DataGridViewTextBoxColumn());
			   this->V22 = (gcnew System::Windows::Forms::DataGridViewTextBoxColumn());
			   this->V2i = (gcnew System::Windows::Forms::DataGridViewTextBoxColumn());
			   this->Column1 = (gcnew System::Windows::Forms::DataGridViewTextBoxColumn());
			   this->Vi2i = (gcnew System::Windows::Forms::DataGridViewTextBoxColumn());
			   this->Column2 = (gcnew System::Windows::Forms::DataGridViewTextBoxColumn());
			   this->OLP = (gcnew System::Windows::Forms::DataGridViewTextBoxColumn());
			   this->Hi = (gcnew System::Windows::Forms::DataGridViewTextBoxColumn());
			   this->C1 = (gcnew System::Windows::Forms::DataGridViewTextBoxColumn());
			   this->C2 = (gcnew System::Windows::Forms::DataGridViewTextBoxColumn());
			   this->label_e = (gcnew System::Windows::Forms::Label());
			   this->textBox_e = (gcnew System::Windows::Forms::TextBox());
			   this->label_u0 = (gcnew System::Windows::Forms::Label());
			   this->textBox_u0 = (gcnew System::Windows::Forms::TextBox());
			   this->label_x0 = (gcnew System::Windows::Forms::Label());
			   this->textBox_x0 = (gcnew System::Windows::Forms::TextBox());
			   this->textBox_kol_vo_shag = (gcnew System::Windows::Forms::TextBox());
			   this->label_kol_vo_shagov = (gcnew System::Windows::Forms::Label());
			   this->textBox_h = (gcnew System::Windows::Forms::TextBox());
			   this->label_h = (gcnew System::Windows::Forms::Label());
			   this->label_Xmax = (gcnew System::Windows::Forms::Label());
			   this->textBox_Xmax = (gcnew System::Windows::Forms::TextBox());
			   this->label1 = (gcnew System::Windows::Forms::Label());
			   this->label2 = (gcnew System::Windows::Forms::Label());
			   this->comboBox2 = (gcnew System::Windows::Forms::ComboBox());
			   this->label6 = (gcnew System::Windows::Forms::Label());
			   this->label4 = (gcnew System::Windows::Forms::Label());
			   this->zedGraphControl2 = (gcnew ZedGraph::ZedGraphControl());
			   this->label3 = (gcnew System::Windows::Forms::Label());
			   this->label5 = (gcnew System::Windows::Forms::Label());
			   this->textBox1 = (gcnew System::Windows::Forms::TextBox());
			   this->pictureBox1 = (gcnew System::Windows::Forms::PictureBox());
			   this->label7 = (gcnew System::Windows::Forms::Label());
			   this->textBox2 = (gcnew System::Windows::Forms::TextBox());
			   this->label8 = (gcnew System::Windows::Forms::Label());
			   this->label9 = (gcnew System::Windows::Forms::Label());
			   this->label10 = (gcnew System::Windows::Forms::Label());
			   this->label11 = (gcnew System::Windows::Forms::Label());
			   (cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->dataGridView1))->BeginInit();
			   (cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->pictureBox1))->BeginInit();
			   this->SuspendLayout();
			   // 
			   // zedGraphControl1
			   // 
			   this->zedGraphControl1->Location = System::Drawing::Point(12, 322);
			   this->zedGraphControl1->Margin = System::Windows::Forms::Padding(5);
			   this->zedGraphControl1->Name = L"zedGraphControl1";
			   this->zedGraphControl1->ScrollGrace = 0;
			   this->zedGraphControl1->ScrollMaxX = 0;
			   this->zedGraphControl1->ScrollMaxY = 0;
			   this->zedGraphControl1->ScrollMaxY2 = 0;
			   this->zedGraphControl1->ScrollMinX = 0;
			   this->zedGraphControl1->ScrollMinY = 0;
			   this->zedGraphControl1->ScrollMinY2 = 0;
			   this->zedGraphControl1->Size = System::Drawing::Size(581, 358);
			   this->zedGraphControl1->TabIndex = 0;
			   this->zedGraphControl1->Load += gcnew System::EventHandler(this, &MyForm::zedGraphControl1_Load);
			   // 
			   // butt_draw
			   // 
			   this->butt_draw->BackColor = System::Drawing::Color::Silver;
			   this->butt_draw->FlatStyle = System::Windows::Forms::FlatStyle::Flat;
			   this->butt_draw->ForeColor = System::Drawing::SystemColors::ControlText;
			   this->butt_draw->Location = System::Drawing::Point(641, 239);
			   this->butt_draw->Margin = System::Windows::Forms::Padding(4);
			   this->butt_draw->Name = L"butt_draw";
			   this->butt_draw->Size = System::Drawing::Size(144, 42);
			   this->butt_draw->TabIndex = 1;
			   this->butt_draw->Text = L"Нарисовать";
			   this->butt_draw->UseVisualStyleBackColor = false;
			   this->butt_draw->Click += gcnew System::EventHandler(this, &MyForm::button1_Click);
			   // 
			   // dataGridView1
			   // 
			   this->dataGridView1->BackgroundColor = System::Drawing::SystemColors::ButtonFace;
			   this->dataGridView1->ColumnHeadersHeightSizeMode = System::Windows::Forms::DataGridViewColumnHeadersHeightSizeMode::AutoSize;
			   this->dataGridView1->Columns->AddRange(gcnew cli::array< System::Windows::Forms::DataGridViewColumn^  >(12) {
				   this->i, this->idXi,
					   this->idVi, this->V22, this->V2i, this->Column1, this->Vi2i, this->Column2, this->OLP, this->Hi, this->C1, this->C2
			   });
			   this->dataGridView1->Location = System::Drawing::Point(824, 80);
			   this->dataGridView1->Margin = System::Windows::Forms::Padding(4);
			   this->dataGridView1->Name = L"dataGridView1";
			   this->dataGridView1->RowHeadersVisible = false;
			   this->dataGridView1->RowHeadersWidth = 51;
			   this->dataGridView1->Size = System::Drawing::Size(412, 201);
			   this->dataGridView1->TabIndex = 2;
			   this->dataGridView1->CellContentClick += gcnew System::Windows::Forms::DataGridViewCellEventHandler(this, &MyForm::dataGridView1_CellContentClick);
			   // 
			   // i
			   // 
			   this->i->HeaderText = L"№i";
			   this->i->MinimumWidth = 6;
			   this->i->Name = L"i";
			   this->i->ReadOnly = true;
			   this->i->Width = 45;
			   // 
			   // idXi
			   // 
			   this->idXi->HeaderText = L"Xi";
			   this->idXi->MinimumWidth = 6;
			   this->idXi->Name = L"idXi";
			   this->idXi->ReadOnly = true;
			   this->idXi->Width = 45;
			   // 
			   // idVi
			   // 
			   this->idVi->HeaderText = L"Vi";
			   this->idVi->MinimumWidth = 6;
			   this->idVi->Name = L"idVi";
			   this->idVi->ReadOnly = true;
			   this->idVi->Resizable = System::Windows::Forms::DataGridViewTriState::True;
			   this->idVi->Width = 45;
			   // 
			   // V22
			   // 
			   this->V22->HeaderText = L"Vi\'";
			   this->V22->MinimumWidth = 6;
			   this->V22->Name = L"V22";
			   this->V22->Width = 45;
			   // 
			   // V2i
			   // 
			   this->V2i->HeaderText = L"V2i";
			   this->V2i->MinimumWidth = 6;
			   this->V2i->Name = L"V2i";
			   this->V2i->Width = 45;
			   // 
			   // Column1
			   // 
			   this->Column1->HeaderText = L"V2i\'";
			   this->Column1->MinimumWidth = 6;
			   this->Column1->Name = L"Column1";
			   this->Column1->Width = 45;
			   // 
			   // Vi2i
			   // 
			   this->Vi2i->HeaderText = L"Vi-V2i";
			   this->Vi2i->MinimumWidth = 6;
			   this->Vi2i->Name = L"Vi2i";
			   this->Vi2i->Width = 45;
			   // 
			   // Column2
			   // 
			   this->Column2->HeaderText = L"Vi\'-V2i\'";
			   this->Column2->MinimumWidth = 6;
			   this->Column2->Name = L"Column2";
			   this->Column2->Width = 45;
			   // 
			   // OLP
			   // 
			   this->OLP->HeaderText = L"OLP";
			   this->OLP->MinimumWidth = 6;
			   this->OLP->Name = L"OLP";
			   this->OLP->Width = 45;
			   // 
			   // Hi
			   // 
			   this->Hi->HeaderText = L"hi";
			   this->Hi->MinimumWidth = 6;
			   this->Hi->Name = L"Hi";
			   this->Hi->Width = 45;
			   // 
			   // C1
			   // 
			   this->C1->HeaderText = L"C1";
			   this->C1->MinimumWidth = 6;
			   this->C1->Name = L"C1";
			   this->C1->Width = 45;
			   // 
			   // C2
			   // 
			   this->C2->HeaderText = L"C2";
			   this->C2->MinimumWidth = 6;
			   this->C2->Name = L"C2";
			   this->C2->Width = 45;
			   // 
			   // label_e
			   // 
			   this->label_e->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 16.2F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(204)));
			   this->label_e->Location = System::Drawing::Point(452, 216);
			   this->label_e->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
			   this->label_e->Name = L"label_e";
			   this->label_e->Size = System::Drawing::Size(95, 32);
			   this->label_e->TabIndex = 3;
			   this->label_e->Text = L"eps:";
			   this->label_e->Click += gcnew System::EventHandler(this, &MyForm::label1_Click);
			   // 
			   // textBox_e
			   // 
			   this->textBox_e->Location = System::Drawing::Point(456, 259);
			   this->textBox_e->Margin = System::Windows::Forms::Padding(4);
			   this->textBox_e->Name = L"textBox_e";
			   this->textBox_e->Size = System::Drawing::Size(145, 22);
			   this->textBox_e->TabIndex = 4;
			   this->textBox_e->Text = L"0,0001";
			   this->textBox_e->TextChanged += gcnew System::EventHandler(this, &MyForm::textBox1_TextChanged);
			   // 
			   // label_u0
			   // 
			   this->label_u0->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 16.2F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(204)));
			   this->label_u0->Location = System::Drawing::Point(452, 148);
			   this->label_u0->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
			   this->label_u0->Name = L"label_u0";
			   this->label_u0->Size = System::Drawing::Size(58, 30);
			   this->label_u0->TabIndex = 5;
			   this->label_u0->Text = L"u₀:";
			   this->label_u0->Click += gcnew System::EventHandler(this, &MyForm::label_u0_Click);
			   // 
			   // textBox_u0
			   // 
			   this->textBox_u0->Location = System::Drawing::Point(456, 188);
			   this->textBox_u0->Margin = System::Windows::Forms::Padding(4);
			   this->textBox_u0->Name = L"textBox_u0";
			   this->textBox_u0->Size = System::Drawing::Size(145, 22);
			   this->textBox_u0->TabIndex = 6;
			   this->textBox_u0->Text = L"1";
			   // 
			   // label_x0
			   // 
			   this->label_x0->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 16.2F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(204)));
			   this->label_x0->Location = System::Drawing::Point(452, 80);
			   this->label_x0->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
			   this->label_x0->Name = L"label_x0";
			   this->label_x0->Size = System::Drawing::Size(51, 32);
			   this->label_x0->TabIndex = 7;
			   this->label_x0->Text = L"x₀:";
			   this->label_x0->Click += gcnew System::EventHandler(this, &MyForm::label_x0_Click);
			   // 
			   // textBox_x0
			   // 
			   this->textBox_x0->Location = System::Drawing::Point(457, 122);
			   this->textBox_x0->Margin = System::Windows::Forms::Padding(4);
			   this->textBox_x0->Name = L"textBox_x0";
			   this->textBox_x0->Size = System::Drawing::Size(144, 22);
			   this->textBox_x0->TabIndex = 8;
			   this->textBox_x0->Text = L"0";
			   // 
			   // textBox_kol_vo_shag
			   // 
			   this->textBox_kol_vo_shag->Location = System::Drawing::Point(281, 122);
			   this->textBox_kol_vo_shag->Margin = System::Windows::Forms::Padding(4);
			   this->textBox_kol_vo_shag->Name = L"textBox_kol_vo_shag";
			   this->textBox_kol_vo_shag->Size = System::Drawing::Size(144, 22);
			   this->textBox_kol_vo_shag->TabIndex = 13;
			   this->textBox_kol_vo_shag->Text = L"10";
			   this->textBox_kol_vo_shag->TextChanged += gcnew System::EventHandler(this, &MyForm::textBox_kol_vo_shag_TextChanged);
			   // 
			   // label_kol_vo_shagov
			   // 
			   this->label_kol_vo_shagov->AutoSize = true;
			   this->label_kol_vo_shagov->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 16.2F, System::Drawing::FontStyle::Regular,
				   System::Drawing::GraphicsUnit::Point, static_cast<System::Byte>(204)));
			   this->label_kol_vo_shagov->Location = System::Drawing::Point(275, 80);
			   this->label_kol_vo_shagov->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
			   this->label_kol_vo_shagov->Name = L"label_kol_vo_shagov";
			   this->label_kol_vo_shagov->Size = System::Drawing::Size(39, 32);
			   this->label_kol_vo_shagov->TabIndex = 12;
			   this->label_kol_vo_shagov->Text = L"n:";
			   // 
			   // textBox_h
			   // 
			   this->textBox_h->Location = System::Drawing::Point(281, 188);
			   this->textBox_h->Margin = System::Windows::Forms::Padding(4);
			   this->textBox_h->Name = L"textBox_h";
			   this->textBox_h->Size = System::Drawing::Size(144, 22);
			   this->textBox_h->TabIndex = 11;
			   this->textBox_h->Text = L"0,001";
			   this->textBox_h->TextChanged += gcnew System::EventHandler(this, &MyForm::textBox5_TextChanged);
			   // 
			   // label_h
			   // 
			   this->label_h->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 16.2F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(204)));
			   this->label_h->Location = System::Drawing::Point(275, 148);
			   this->label_h->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
			   this->label_h->Name = L"label_h";
			   this->label_h->Size = System::Drawing::Size(61, 36);
			   this->label_h->TabIndex = 10;
			   this->label_h->Text = L"h₀:";
			   this->label_h->Click += gcnew System::EventHandler(this, &MyForm::label_h_Click);
			   // 
			   // label_Xmax
			   // 
			   this->label_Xmax->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 16.2F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(204)));
			   this->label_Xmax->Location = System::Drawing::Point(275, 225);
			   this->label_Xmax->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
			   this->label_Xmax->Name = L"label_Xmax";
			   this->label_Xmax->Size = System::Drawing::Size(102, 30);
			   this->label_Xmax->TabIndex = 16;
			   this->label_Xmax->Text = L"Xmax:";
			   // 
			   // textBox_Xmax
			   // 
			   this->textBox_Xmax->Location = System::Drawing::Point(280, 259);
			   this->textBox_Xmax->Margin = System::Windows::Forms::Padding(4);
			   this->textBox_Xmax->Name = L"textBox_Xmax";
			   this->textBox_Xmax->Size = System::Drawing::Size(145, 22);
			   this->textBox_Xmax->TabIndex = 17;
			   this->textBox_Xmax->Text = L"5";
			   // 
			   // label1
			   // 
			   this->label1->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 19.8F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(204)));
			   this->label1->Location = System::Drawing::Point(484, -8);
			   this->label1->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
			   this->label1->MaximumSize = System::Drawing::Size(451, 400);
			   this->label1->Name = L"label1";
			   this->label1->Size = System::Drawing::Size(355, 56);
			   this->label1->TabIndex = 23;
			   this->label1->Text = L"2-я основная задача";
			   this->label1->Click += gcnew System::EventHandler(this, &MyForm::label1_Click_1);
			   // 
			   // label2
			   // 
			   this->label2->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 16.2F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(204)));
			   this->label2->Location = System::Drawing::Point(6, 237);
			   this->label2->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
			   this->label2->MaximumSize = System::Drawing::Size(251, 150);
			   this->label2->Name = L"label2";
			   this->label2->Size = System::Drawing::Size(119, 30);
			   this->label2->TabIndex = 24;
			   this->label2->Text = L"Версия";
			   this->label2->Click += gcnew System::EventHandler(this, &MyForm::label2_Click);
			   // 
			   // comboBox2
			   // 
			   this->comboBox2->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(204)));
			   this->comboBox2->FormattingEnabled = true;
			   this->comboBox2->Items->AddRange(gcnew cli::array< System::Object^  >(2) { L"Без контроля ЛП", L"С контролем ЛП" });
			   this->comboBox2->Location = System::Drawing::Point(12, 269);
			   this->comboBox2->Margin = System::Windows::Forms::Padding(3, 2, 3, 2);
			   this->comboBox2->Name = L"comboBox2";
			   this->comboBox2->Size = System::Drawing::Size(193, 33);
			   this->comboBox2->TabIndex = 25;
			   // 
			   // label6
			   // 
			   this->label6->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(204)));
			   this->label6->Location = System::Drawing::Point(726, 655);
			   this->label6->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
			   this->label6->MaximumSize = System::Drawing::Size(500, 550);
			   this->label6->Name = L"label6";
			   this->label6->Size = System::Drawing::Size(346, 22);
			   this->label6->TabIndex = 33;
			   this->label6->Click += gcnew System::EventHandler(this, &MyForm::label6_Click);
			   // 
			   // label4
			   // 
			   this->label4->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 12, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(204)));
			   this->label4->Location = System::Drawing::Point(1089, 658);
			   this->label4->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
			   this->label4->MaximumSize = System::Drawing::Size(500, 550);
			   this->label4->Name = L"label4";
			   this->label4->Size = System::Drawing::Size(347, 22);
			   this->label4->TabIndex = 35;
			   this->label4->Click += gcnew System::EventHandler(this, &MyForm::label4_Click);
			   // 
			   // zedGraphControl2
			   // 
			   this->zedGraphControl2->Location = System::Drawing::Point(655, 322);
			   this->zedGraphControl2->Margin = System::Windows::Forms::Padding(5);
			   this->zedGraphControl2->Name = L"zedGraphControl2";
			   this->zedGraphControl2->ScrollGrace = 0;
			   this->zedGraphControl2->ScrollMaxX = 0;
			   this->zedGraphControl2->ScrollMaxY = 0;
			   this->zedGraphControl2->ScrollMaxY2 = 0;
			   this->zedGraphControl2->ScrollMinX = 0;
			   this->zedGraphControl2->ScrollMinY = 0;
			   this->zedGraphControl2->ScrollMinY2 = 0;
			   this->zedGraphControl2->Size = System::Drawing::Size(581, 358);
			   this->zedGraphControl2->TabIndex = 36;
			   // 
			   // label3
			   // 
			   this->label3->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 16.2F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(204)));
			   this->label3->Location = System::Drawing::Point(-8, 82);
			   this->label3->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
			   this->label3->MaximumSize = System::Drawing::Size(251, 150);
			   this->label3->Name = L"label3";
			   this->label3->Size = System::Drawing::Size(237, 30);
			   this->label3->TabIndex = 39;
			   this->label3->Text = L"Задача Коши:";
			   this->label3->Click += gcnew System::EventHandler(this, &MyForm::label3_Click_1);
			   // 
			   // label5
			   // 
			   this->label5->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 16.2F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(204)));
			   this->label5->Location = System::Drawing::Point(635, 80);
			   this->label5->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
			   this->label5->Name = L"label5";
			   this->label5->Size = System::Drawing::Size(51, 32);
			   this->label5->TabIndex = 40;
			   this->label5->Text = L"a:";
			   // 
			   // textBox1
			   // 
			   this->textBox1->Location = System::Drawing::Point(641, 122);
			   this->textBox1->Margin = System::Windows::Forms::Padding(4);
			   this->textBox1->Name = L"textBox1";
			   this->textBox1->Size = System::Drawing::Size(144, 22);
			   this->textBox1->TabIndex = 41;
			   this->textBox1->Text = L"5";
			   // 
			   // pictureBox1
			   // 
			   this->pictureBox1->Image = (cli::safe_cast<System::Drawing::Image^>(resources->GetObject(L"pictureBox1.Image")));
			   this->pictureBox1->Location = System::Drawing::Point(-2, 122);
			   this->pictureBox1->Name = L"pictureBox1";
			   this->pictureBox1->Size = System::Drawing::Size(276, 121);
			   this->pictureBox1->TabIndex = 42;
			   this->pictureBox1->TabStop = false;
			   // 
			   // label7
			   // 
			   this->label7->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 16.2F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(204)));
			   this->label7->Location = System::Drawing::Point(635, 148);
			   this->label7->Margin = System::Windows::Forms::Padding(4, 0, 4, 0);
			   this->label7->Name = L"label7";
			   this->label7->Size = System::Drawing::Size(58, 30);
			   this->label7->TabIndex = 43;
			   this->label7->Text = L"u₀\':";
			   // 
			   // textBox2
			   // 
			   this->textBox2->Location = System::Drawing::Point(640, 188);
			   this->textBox2->Margin = System::Windows::Forms::Padding(4);
			   this->textBox2->Name = L"textBox2";
			   this->textBox2->Size = System::Drawing::Size(145, 22);
			   this->textBox2->TabIndex = 44;
			   this->textBox2->Text = L"1";
			   // 
			   // label8
			   // 
			   this->label8->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 10.2F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(204)));
			   this->label8->Location = System::Drawing::Point(12, 704);
			   this->label8->MaximumSize = System::Drawing::Size(300, 100);
			   this->label8->Name = L"label8";
			   this->label8->RightToLeft = System::Windows::Forms::RightToLeft::No;
			   this->label8->Size = System::Drawing::Size(300, 30);
			   this->label8->TabIndex = 45;
			   this->label8->Click += gcnew System::EventHandler(this, &MyForm::label8_Click);
			   // 
			   // label9
			   // 
			   this->label9->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 10.2F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(204)));
			   this->label9->Location = System::Drawing::Point(12, 763);
			   this->label9->MaximumSize = System::Drawing::Size(300, 100);
			   this->label9->Name = L"label9";
			   this->label9->RightToLeft = System::Windows::Forms::RightToLeft::No;
			   this->label9->Size = System::Drawing::Size(300, 30);
			   this->label9->TabIndex = 46;
			   this->label9->Click += gcnew System::EventHandler(this, &MyForm::label9_Click);
			   // 
			   // label10
			   // 
			   this->label10->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 10.2F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(204)));
			   this->label10->Location = System::Drawing::Point(651, 704);
			   this->label10->MaximumSize = System::Drawing::Size(300, 100);
			   this->label10->Name = L"label10";
			   this->label10->RightToLeft = System::Windows::Forms::RightToLeft::No;
			   this->label10->Size = System::Drawing::Size(300, 30);
			   this->label10->TabIndex = 47;
			   this->label10->Click += gcnew System::EventHandler(this, &MyForm::label10_Click);
			   // 
			   // label11
			   // 
			   this->label11->Font = (gcnew System::Drawing::Font(L"Microsoft Sans Serif", 10.2F, System::Drawing::FontStyle::Regular, System::Drawing::GraphicsUnit::Point,
				   static_cast<System::Byte>(204)));
			   this->label11->Location = System::Drawing::Point(651, 753);
			   this->label11->Name = L"label11";
			   this->label11->Size = System::Drawing::Size(300, 30);
			   this->label11->TabIndex = 48;
			   this->label11->Click += gcnew System::EventHandler(this, &MyForm::label11_Click);
			   // 
			   // MyForm
			   // 
			   this->AutoScaleDimensions = System::Drawing::SizeF(8, 16);
			   this->AutoScaleMode = System::Windows::Forms::AutoScaleMode::Font;
			   this->BackColor = System::Drawing::SystemColors::InactiveCaption;
			   this->ClientSize = System::Drawing::Size(1265, 802);
			   this->Controls->Add(this->label11);
			   this->Controls->Add(this->label10);
			   this->Controls->Add(this->label9);
			   this->Controls->Add(this->label8);
			   this->Controls->Add(this->textBox2);
			   this->Controls->Add(this->label7);
			   this->Controls->Add(this->pictureBox1);
			   this->Controls->Add(this->textBox1);
			   this->Controls->Add(this->label5);
			   this->Controls->Add(this->label3);
			   this->Controls->Add(this->zedGraphControl2);
			   this->Controls->Add(this->label4);
			   this->Controls->Add(this->label6);
			   this->Controls->Add(this->comboBox2);
			   this->Controls->Add(this->label2);
			   this->Controls->Add(this->label1);
			   this->Controls->Add(this->textBox_Xmax);
			   this->Controls->Add(this->label_Xmax);
			   this->Controls->Add(this->textBox_kol_vo_shag);
			   this->Controls->Add(this->label_kol_vo_shagov);
			   this->Controls->Add(this->textBox_h);
			   this->Controls->Add(this->label_h);
			   this->Controls->Add(this->textBox_x0);
			   this->Controls->Add(this->label_x0);
			   this->Controls->Add(this->textBox_u0);
			   this->Controls->Add(this->label_u0);
			   this->Controls->Add(this->textBox_e);
			   this->Controls->Add(this->label_e);
			   this->Controls->Add(this->dataGridView1);
			   this->Controls->Add(this->butt_draw);
			   this->Controls->Add(this->zedGraphControl1);
			   this->ForeColor = System::Drawing::SystemColors::ActiveCaptionText;
			   this->Margin = System::Windows::Forms::Padding(4);
			   this->Name = L"MyForm";
			   this->Text = L"MyForm";
			   this->Load += gcnew System::EventHandler(this, &MyForm::MyForm_Load);
			   (cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->dataGridView1))->EndInit();
			   (cli::safe_cast<System::ComponentModel::ISupportInitialize^>(this->pictureBox1))->EndInit();
			   this->ResumeLayout(false);
			   this->PerformLayout();

		   }
#pragma endregion
	private:
		double f1(double x, double u0, double x0) {
			return exp(3 * x) * u0 / exp(3 * x0);
		}

	private: System::Void button1_Click(System::Object^ sender, System::EventArgs^ e) {
		int error = comboBox2->SelectedIndex;

		GraphPane^ panel = zedGraphControl1->GraphPane;
		panel->CurveList->Clear();

		GraphPane^ panelph = zedGraphControl2->GraphPane;
		panelph->CurveList->Clear();

		PointPairList^ f1_list = gcnew ZedGraph::PointPairList();
		PointPairList^ f2_list = gcnew ZedGraph::PointPairList();
		PointPairList^ f3_list = gcnew ZedGraph::PointPairList();
		int length = 2;

		vector<double> U(length), half(length), LP(length + 2);
		vector<int> count(2);

		double eps = Convert::ToDouble(textBox_e->Text);
		U[0] = Convert::ToDouble(textBox_u0->Text);
		U[1] = Convert::ToDouble(textBox2->Text);
		double xmin = Convert::ToDouble(textBox_x0->Text);
		double xmax = Convert::ToDouble(textBox_Xmax->Text);
		double h = Convert::ToDouble(textBox_h->Text);
		int n = Convert::ToInt32(textBox_kol_vo_shag->Text);
		double a = Convert::ToDouble(textBox1->Text);


		double xmin_limit = xmin - 0.1;
		double xmax_limit = xmax + 0.1;
		double x = xmin;
		double Maxh = h, Minh = h, MaxOLP = 0;
		double start = U[0];

		func Solution(xmin, U, h, error);
		Solution.GetParamerts(a);

		start = U[0];
		dataGridView1->Rows->Clear();

		//double maxOlp = -DBL_MAX, maxHi = -DBL_MAX, XmaxminusX = 0, minHi = -DBL_MIN, maxxi = -DBL_MAX;
		zedGraphControl2->Visible = true;
		if (error == 0)
		{

			for (int i = 0; (i < n) && (x < xmax); i++)
			{
				//Добавление в список точек для графика
				f1_list->Add(x, U[0]);
				f2_list->Add(x, U[1]);
				f3_list->Add(U[0], U[1]);
				//Печать в таблицу
				dataGridView1->Rows->Add();
				dataGridView1->Rows[i]->Cells[0]->Value = i;
				dataGridView1->Rows[i]->Cells[1]->Value = x;
				dataGridView1->Rows[i]->Cells[2]->Value = U[0];
				dataGridView1->Rows[i]->Cells[3]->Value = U[1];
				dataGridView1->Rows[i]->Cells[5]->Value = h;
				U = Solution.RunKut4(x, U, h);
				x = x + h;
			}
		}
		else
		{
			for (int i = 0; (i < n) && (x < xmax); i++)
			{
				//Добавление на график
				f1_list->Add(x, U[0]);
				f2_list->Add(x, U[1]);
				f3_list->Add(U[0], U[1]);
				//Печать в таблицу
				dataGridView1->Rows->Add();
				dataGridView1->Rows[i]->Cells[0]->Value = i;
				dataGridView1->Rows[i]->Cells[1]->Value = x;
				dataGridView1->Rows[i]->Cells[2]->Value = U[0];
				dataGridView1->Rows[i]->Cells[3]->Value = U[1];
				dataGridView1->Rows[i]->Cells[4]->Value = LP[0];
				dataGridView1->Rows[i]->Cells[5]->Value = LP[1];
				dataGridView1->Rows[i]->Cells[6]->Value = U[0] - LP[0];
				dataGridView1->Rows[i]->Cells[7]->Value = U[1] - LP[1];
				dataGridView1->Rows[i]->Cells[8]->Value = LP[length + 1];
				dataGridView1->Rows[i]->Cells[9]->Value = h;
				dataGridView1->Rows[i]->Cells[10]->Value = count[0];
				dataGridView1->Rows[i]->Cells[11]->Value = count[1];
				half = U;
				U = Solution.RunKut4(x, U, h);
				LP = Solution.LocalErrorControl(U, half, h, x);
				if (h / 2 == LP[length])
				{
					U = half;
					x = x - h;
					count[0]++;
					if (LP[length] < Minh)
						Minh = LP[length];
				}
				if (2 * h == LP[length])
				{
					count[1]++;
					if (LP[length] > Maxh)
						Maxh = LP[length];
				}
				if (abs(LP[length + 1]) > MaxOLP)
					MaxOLP = abs(LP[length + 1]);
				x = x + h;
				h = LP[length];
			}
		}

		LineItem^ f1_Curve = panel->AddCurve("U(x)", f1_list, Color::Orange, SymbolType::None);
		LineItem^ f2_Curve = panel->AddCurve("U'(x)", f2_list, Color::Purple, SymbolType::None);
		LineItem^ f3_Curve = panelph->AddCurve("FP", f3_list, Color::Cyan, SymbolType::None);


		label8->Text = "Xmax - X = " + Convert::ToString(xmax - x);
		label9->Text = "max OLP = " + Convert::ToString(MaxOLP);
		label10->Text = "max H = " + Convert::ToString(Maxh);
		label11->Text = "min H = " + Convert::ToString(Minh);




		panel->YAxisList->Clear();

		int axis1 = panel->AddYAxis("Ось U");
		int axis2 = panel->AddYAxis("Ось U'");

		f1_Curve->YAxisIndex = axis1;
		f2_Curve->YAxisIndex = axis2;

		panel->YAxisList[axis1]->Title->FontSpec->FontColor = Color::Orange;
		panel->YAxisList[axis2]->Title->FontSpec->FontColor = Color::Purple;


		panel->YAxis->Scale->Min = -5;
		panel->YAxis->Scale->Max = 5;
		panel->XAxis->Scale->Min = xmin - 0.1;
		panel->XAxis->Scale->Max = xmax + 0.1;

		// Обновляем график, обновляем оси
		zedGraphControl1->AxisChange();
		zedGraphControl1->Invalidate();
		zedGraphControl2->AxisChange();
		zedGraphControl2->Invalidate();


		// Вызываем метод AxisChange (), чтобы обновить данные об осях. 
		// В противном случае на рисунке будет показана только часть графика, 
		// которая умещается в интервалы по осям, установленные по умолчанию
		zedGraphControl1->AxisChange();
		// Обновляем график
		zedGraphControl1->Invalidate();

	}
	private: System::Void zedGraphControl1_Load(System::Object^ sender, System::EventArgs^ e) {
	}

	private: void DrawGraph()
	{

		GraphPane^ panel = zedGraphControl1->GraphPane;
		GraphPane^ panelph = zedGraphControl2->GraphPane;

		panel->XAxis->Title->Text = "Ось X";
		panel->YAxis->Title->Text = "Ось U";
		panelph->XAxis->Title->Text = "Ось U";
		panelph->YAxis->Title->Text = "Ось U'";

		panel->Title->Text = "Рисунок";
		panelph->Title->Text = "Фазовый портрет";


		zedGraphControl1->AxisChange();
		zedGraphControl1->Invalidate();
		zedGraphControl2->AxisChange();
		zedGraphControl2->Invalidate();


	}
	private: System::Void dataGridView1_CellContentClick(System::Object^ sender, System::Windows::Forms::DataGridViewCellEventArgs^ e) {
	}
	private: System::Void label1_Click(System::Object^ sender, System::EventArgs^ e) {
	}
	private: System::Void textBox1_TextChanged(System::Object^ sender, System::EventArgs^ e) {
	}
	private: System::Void textBox5_TextChanged(System::Object^ sender, System::EventArgs^ e) {
	}
	private: System::Void label_u0_Click(System::Object^ sender, System::EventArgs^ e) {
	}
	private: System::Void MyForm_Load(System::Object^ sender, System::EventArgs^ e) {
	}
	private: System::Void label1_Click_1(System::Object^ sender, System::EventArgs^ e) {
	}
	private: System::Void comboBox1_SelectedIndexChanged(System::Object^ sender, System::EventArgs^ e) {
	}
	private: System::Void label3_Click(System::Object^ sender, System::EventArgs^ e) {
	}
	private: System::Void label6_Click(System::Object^ sender, System::EventArgs^ e) {
	}
	private: System::Void label4_Click(System::Object^ sender, System::EventArgs^ e) {
	}
	private: System::Void textBox_kol_vo_shag_TextChanged(System::Object^ sender, System::EventArgs^ e) {
	}
	private: System::Void label3_Click_1(System::Object^ sender, System::EventArgs^ e) {
	}
	private: System::Void label_h_Click(System::Object^ sender, System::EventArgs^ e) {
	}
	private: System::Void label_x0_Click(System::Object^ sender, System::EventArgs^ e) {
	}
	private: System::Void pictureBox2_Click(System::Object^ sender, System::EventArgs^ e) {
	}
	private: System::Void label2_Click(System::Object^ sender, System::EventArgs^ e) {
	}
	private: System::Void label9_Click(System::Object^ sender, System::EventArgs^ e) {
	}
	private: System::Void label8_Click(System::Object^ sender, System::EventArgs^ e) {
	}
	private: System::Void label11_Click(System::Object^ sender, System::EventArgs^ e) {
	}
	private: System::Void label10_Click(System::Object^ sender, System::EventArgs^ e) {
	}
	};
}
