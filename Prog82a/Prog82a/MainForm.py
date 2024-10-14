import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(250, 79)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(186, 35)
        self._textBox1.TabIndex = 0
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Modern No. 20", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(48, 38)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(163, 26)
        self._label1.TabIndex = 2
        self._label1.Text = "Speed Limit"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Modern No. 20", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(48, 75)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(196, 26)
        self._label2.TabIndex = 3
        self._label2.Text = "Recorded Speed"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(250, 38)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(186, 35)
        self._textBox3.TabIndex = 4
        self._textBox3.TextChanged += self.TextBox3TextChanged
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self._button1.Font = System.Drawing.Font("Modern No. 20", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(48, 210)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(75, 70)
        self._button1.TabIndex = 5
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self._button2.Font = System.Drawing.Font("Modern No. 20", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(208, 210)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(75, 70)
        self._button2.TabIndex = 6
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self._button3.Font = System.Drawing.Font("Modern No. 20", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(361, 210)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(75, 70)
        self._button3.TabIndex = 7
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Modern No. 20", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(250, 128)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(155, 56)
        self._label3.TabIndex = 8
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Modern No. 20", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(48, 127)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(196, 26)
        self._label4.TabIndex = 9
        self._label4.Text = "Fine Amount ($)"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label4.Click += self.Label4Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Gray
        self.ClientSize = System.Drawing.Size(492, 299)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Prog82a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        spd = int(self._textBox1.Text)
        spdlmt = int(self._textBox3.Text)
        dif = spd - spdlmt
        fine = 20 + (dif * 5)
        self._label3.Text = str(fine)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox3.Text = ""
        self._label3.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def Label4Click(self, sender, e):
        pass

    def TextBox3TextChanged(self, sender, e):
        pass