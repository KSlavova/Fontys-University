namespace CarApplication
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            label1 = new Label();
            label2 = new Label();
            Brand1 = new TextBox();
            Speed1 = new TextBox();
            Brand2 = new TextBox();
            Speed2 = new TextBox();
            label3 = new Label();
            label4 = new Label();
            InfoFirstCar = new Label();
            SpeedFirstCar = new Button();
            SlowFirstCar = new Button();
            SpeedSecondCar = new Button();
            SlowSecondCar = new Button();
            InfoSecondCar = new Label();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(39, 54);
            label1.Name = "label1";
            label1.Size = new Size(62, 25);
            label1.TabIndex = 0;
            label1.Text = "Brand:";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(36, 90);
            label2.Name = "label2";
            label2.Size = new Size(150, 25);
            label2.TabIndex = 1;
            label2.Text = "Maximum Speed:";
            // 
            // Brand1
            // 
            Brand1.Location = new Point(141, 55);
            Brand1.Name = "Brand1";
            Brand1.Size = new Size(150, 31);
            Brand1.TabIndex = 2;
            // 
            // Speed1
            // 
            Speed1.Location = new Point(192, 90);
            Speed1.Name = "Speed1";
            Speed1.Size = new Size(150, 31);
            Speed1.TabIndex = 3;
            // 
            // Brand2
            // 
            Brand2.Location = new Point(586, 51);
            Brand2.Name = "Brand2";
            Brand2.Size = new Size(150, 31);
            Brand2.TabIndex = 4;
            // 
            // Speed2
            // 
            Speed2.Location = new Point(641, 97);
            Speed2.Name = "Speed2";
            Speed2.Size = new Size(150, 31);
            Speed2.TabIndex = 5;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(485, 51);
            label3.Name = "label3";
            label3.Size = new Size(62, 25);
            label3.TabIndex = 6;
            label3.Text = "Brand:";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(485, 103);
            label4.Name = "label4";
            label4.Size = new Size(150, 25);
            label4.TabIndex = 7;
            label4.Text = "Maximum Speed:";
            // 
            // InfoFirstCar
            // 
            InfoFirstCar.BorderStyle = BorderStyle.Fixed3D;
            InfoFirstCar.Location = new Point(12, 235);
            InfoFirstCar.Name = "InfoFirstCar";
            InfoFirstCar.Size = new Size(502, 25);
            InfoFirstCar.TabIndex = 8;
            InfoFirstCar.Click += InfoFirstCar_Click;
            // 
            // SpeedFirstCar
            // 
            SpeedFirstCar.Location = new Point(12, 318);
            SpeedFirstCar.Name = "SpeedFirstCar";
            SpeedFirstCar.Size = new Size(112, 34);
            SpeedFirstCar.TabIndex = 9;
            SpeedFirstCar.Text = "Accelerate";
            SpeedFirstCar.UseVisualStyleBackColor = true;
            SpeedFirstCar.Click += SpeedFirstCar_Click;
            // 
            // SlowFirstCar
            // 
            SlowFirstCar.Location = new Point(366, 318);
            SlowFirstCar.Name = "SlowFirstCar";
            SlowFirstCar.Size = new Size(141, 34);
            SlowFirstCar.TabIndex = 10;
            SlowFirstCar.Text = "Use the brakes";
            SlowFirstCar.UseVisualStyleBackColor = true;
            SlowFirstCar.Click += SlowFirstCar_Click;
            // 
            // SpeedSecondCar
            // 
            SpeedSecondCar.Location = new Point(597, 318);
            SpeedSecondCar.Name = "SpeedSecondCar";
            SpeedSecondCar.Size = new Size(112, 34);
            SpeedSecondCar.TabIndex = 11;
            SpeedSecondCar.Text = "Accelerate";
            SpeedSecondCar.UseVisualStyleBackColor = true;
            SpeedSecondCar.Click += SpeedSecondCar_Click;
            // 
            // SlowSecondCar
            // 
            SlowSecondCar.Location = new Point(985, 318);
            SlowSecondCar.Name = "SlowSecondCar";
            SlowSecondCar.Size = new Size(142, 34);
            SlowSecondCar.TabIndex = 12;
            SlowSecondCar.Text = "Use the brakes";
            SlowSecondCar.UseVisualStyleBackColor = true;
            SlowSecondCar.Click += SlowSecondCar_Click;
            // 
            // InfoSecondCar
            // 
            InfoSecondCar.BorderStyle = BorderStyle.Fixed3D;
            InfoSecondCar.Location = new Point(597, 235);
            InfoSecondCar.Name = "InfoSecondCar";
            InfoSecondCar.Size = new Size(562, 25);
            InfoSecondCar.TabIndex = 13;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1171, 450);
            Controls.Add(InfoSecondCar);
            Controls.Add(SlowSecondCar);
            Controls.Add(SpeedSecondCar);
            Controls.Add(SlowFirstCar);
            Controls.Add(SpeedFirstCar);
            Controls.Add(InfoFirstCar);
            Controls.Add(label4);
            Controls.Add(label3);
            Controls.Add(Speed2);
            Controls.Add(Brand2);
            Controls.Add(Speed1);
            Controls.Add(Brand1);
            Controls.Add(label2);
            Controls.Add(label1);
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private Label label2;
        private TextBox Brand1;
        private TextBox Speed1;
        private TextBox Brand2;
        private TextBox Speed2;
        private Label label3;
        private Label label4;
        private Label InfoFirstCar;
        private Button SpeedFirstCar;
        private Button SlowFirstCar;
        private Button SpeedSecondCar;
        private Button SlowSecondCar;
        private Label InfoSecondCar;
    }
}
