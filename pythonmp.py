# Import tkinter
from tkinter import *
from PIL import Image,ImageTk

class LoanCalculator:


	def __init__(self):

		window = Tk() # Create a window
		path="calci.png"
		load=Image.open(path)
		render=ImageTk.PhotoImage(load)
		window.iconphoto(False,render)  
		window.configure(bg="#9090EE") 
		window.title("Loan Calculator") # Set title
		window.geometry("400x400")


	
		# create the input boxes.
		Label(window, text = "Annual Interest Rate",justify = LEFT,bg="#E0E0FF",font=('Times',12)).grid(row = 2,
										column = 1, sticky=W)
		Label(window, text = "Number of Years",justify = LEFT,bg="#E0E0FF",font=('Times',12)).grid(row = 3,
									column = 1, sticky=W)
		Label(window, text = "Loan Amount",justify = LEFT,bg="#E0E0FF",font=('Times',12)).grid(row = 4,
								column = 1, sticky=W)
		Label(window, text = "Monthly Payment",justify = LEFT,bg="#E0E0FF",font=('Times',12)).grid(row = 5,
									column = 1, sticky=W)
		Label(window, text = "Total Payment",justify = LEFT,bg="#E0E0FF",font=('Times',12)).grid(row = 6,
									column = 1, sticky=W)

		# for taking inputs
		self.annualInterestRateVar = StringVar()
		Entry(window, textvariable = self.annualInterestRateVar,
					justify = RIGHT,font=('Times',12)).grid(row = 2, column = 2)
		
		self.numberOfYearsVar = StringVar()
		Entry(window, textvariable = self.numberOfYearsVar,
				justify = RIGHT,font=('Times',12)).grid(row = 3, column = 2,pady=25)
		
		self.loanAmountVar = StringVar()
		Entry(window, textvariable = self.loanAmountVar,
			justify = RIGHT,font=('Times',12)).grid(row = 4, column = 2,padx= 25)
		
		self.monthlyPaymentVar = StringVar()
		lblMonthlyPayment = Label(window, textvariable =
						self.monthlyPaymentVar,bg="#9090EE",font=('Times',12)).grid(row = 5,
						column = 2, sticky = E, pady= 25)

		self.totalPaymentVar = StringVar()
		lblTotalPayment = Label(window, textvariable =
					self.totalPaymentVar,bg="#9090EE",font=('Times',12)).grid(row = 6,
					column = 2, sticky = "E")
		
		# create the button
		btComputePayment = Button(window, text = "Compute Payment",command = self.computePayment,bg="#ADADD8",font=('Times',12)).grid(
			row = 7, column = 2, sticky = "E", pady= 25)
		window.mainloop() # Create an event loop


	# compute the total payment.
	def computePayment(self):
				
		monthlyPayment = self.getMonthlyPayment(
		float(self.loanAmountVar.get()),
		float(self.annualInterestRateVar.get()) / 1200,
		int(self.numberOfYearsVar.get()))

		self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
		totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberOfYearsVar.get())

		self.totalPaymentVar.set(format(totalPayment, '10.2f'))

	def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
		# compute the monthly payment.
		monthlyPayment = loanAmount * monthlyInterestRate / (1
		- 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
		return monthlyPayment
		root = Tk() # create the widget
	

# call the class to run the program.

LoanCalculator()
