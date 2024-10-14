import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(9, 5)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(170, 40)
        self._label1.TabIndex = 0
        self._label1.Text = "label1"
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(9, 45)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(170, 40)
        self._label2.TabIndex = 1
        self._label2.Text = "label2"
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(9, 85)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(170, 40)
        self._label3.TabIndex = 2
        self._label3.Text = "label3"
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(167, 5)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(191, 20)
        self._textBox1.TabIndex = 3
        self._textBox1.TextChanged += self.TextBox1TextChanged
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(167, 42)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(191, 20)
        self._textBox2.TabIndex = 4
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(167, 85)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(191, 29)
        self._label4.TabIndex = 5
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(9, 111)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(98, 85)
        self._button1.TabIndex = 6
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(9, 202)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(98, 85)
        self._button2.TabIndex = 7
        self._button2.Text = "button2"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(9, 293)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(98, 85)
        self._button3.TabIndex = 8
        self._button3.Text = "button3"
        self._button3.UseVisualStyleBackColor = True
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(171, 81)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(170, 30)
        self._label5.TabIndex = 9
        self._label5.Text = "label5"
        # 
        # label6
        # 
        self._label6.Location = System.Drawing.Point(171, 111)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(170, 30)
        self._label6.TabIndex = 10
        self._label6.Text = "label6"
        # 
        # label7
        # 
        self._label7.Location = System.Drawing.Point(171, 141)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(170, 30)
        self._label7.TabIndex = 11
        self._label7.Text = "label7"
        # 
        # label8
        # 
        self._label8.Location = System.Drawing.Point(167, 171)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(170, 30)
        self._label8.TabIndex = 12
        self._label8.Text = "label8"
        # 
        # label9
        # 
        self._label9.Location = System.Drawing.Point(167, 201)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(170, 30)
        self._label9.TabIndex = 13
        self._label9.Text = "label9"
        # 
        # label10
        # 
        self._label10.Location = System.Drawing.Point(167, 230)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(170, 57)
        self._label10.TabIndex = 14
        self._label10.Text = "label10"
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(370, 451)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog58t"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def TextBox1TextChanged(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        num1 = int(self._textBox1.Text)
        num2 = int(self._textBox2.Text)
        change = num2 - num1
        nd = int(CL)
        CL
        
    def MainFormLoad(self, sender, e):
        pass