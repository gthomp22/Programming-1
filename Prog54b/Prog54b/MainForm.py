import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(35, 113)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(90, 62)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.Control
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(309, 205)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(277, 54)
        self._label1.TabIndex = 1
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.Control
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(309, 302)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(277, 54)
        self._label2.TabIndex = 2
        self._label2.Click += self.Label2Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(309, 31)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(277, 35)
        self._textBox1.TabIndex = 3
        self._textBox1.TextChanged += self.TextBox1TextChanged
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(309, 113)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(277, 35)
        self._textBox2.TabIndex = 4
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(309, 72)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(277, 35)
        self._textBox3.TabIndex = 4
        # 
        # textBox4
        # 
        self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(309, 154)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(277, 35)
        self._textBox4.TabIndex = 5
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(35, 205)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(90, 62)
        self._button2.TabIndex = 6
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(35, 290)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(90, 62)
        self._button3.TabIndex = 7
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ControlDark
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(193, 205)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(88, 54)
        self._label3.TabIndex = 8
        self._label3.Text = "Sum"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.ControlDark
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(193, 302)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(88, 54)
        self._label5.TabIndex = 10
        self._label5.Text = "Average"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(808, 432)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog54b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label3Click(self, sender, e):
        pass

    def Label2Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        num1 = int(self._textBox1.Text)
        num2 = int(self._textBox2.Text)
        num3 = int(self._textBox3.Text)
        num4 = int(self._textBox4.Text)
        sum  = num1 + num2 + num3 + num4
        average = sum/4.0
        self._label1.Text = str(sum)
        self._label2.Text = str(average)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._label2.Text = ""
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def TextBox1TextChanged(self, sender, e):
        pass