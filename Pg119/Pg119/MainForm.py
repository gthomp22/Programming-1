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
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label1.Location = System.Drawing.Point(20, 22)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(132, 32)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter First Name:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label2.Location = System.Drawing.Point(20, 80)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(132, 32)
        self._label2.TabIndex = 1
        self._label2.Text = "Enter Last Name;"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label3.Location = System.Drawing.Point(20, 151)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(132, 32)
        self._label3.TabIndex = 2
        self._label3.Text = "This Is Your Full Name:"
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.SystemColors.ControlDark
        self._textBox1.Location = System.Drawing.Point(146, 19)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(120, 20)
        self._textBox1.TabIndex = 3
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.SystemColors.ControlDark
        self._textBox2.Location = System.Drawing.Point(146, 80)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(120, 20)
        self._textBox2.TabIndex = 4
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(146, 151)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(132, 32)
        self._label4.TabIndex = 5
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ControlDark
        self._button1.Location = System.Drawing.Point(15, 206)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(99, 24)
        self._button1.TabIndex = 6
        self._button1.Text = "Show Name"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ControlDark
        self._button2.Location = System.Drawing.Point(120, 206)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(99, 24)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.ControlDark
        self._button3.Location = System.Drawing.Point(225, 206)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(99, 24)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self.ClientSize = System.Drawing.Size(350, 261)
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
        self.Text = "Pg119"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def MainFormLoad(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        first = self._textBox1.Text
        last  = self._textBox2.Text
        firstlast = first + " " + last
        self._label4.Text = str(firstlast)
        

    def Button2Click(self, sender, e):
        self._label4.Text   = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()