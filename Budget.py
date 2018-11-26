import tkinter
from tkinter import messagebox



root = tkinter.Tk()
root.configure(bg="lightyellow")
root.title("Python Project")
root.geometry("725x482")



def reset():
    labelEFentry.delete(0,"end")
    labelInvestmentsentry.delete(0,"end")
    labelRetiremententry.delete(0,"end")
    labelFoodentry.delete(0,"end")
    labelClothentry.delete(0,"end")
    labelShelterentry.delete(0,"end")
    labelHouseholdentry.delete(0,"end")
    labelTransportentry.delete(0,"end")
    labelHealthentry.delete(0,"end")
    labelPersonalentry.delete(0,"end")
    labelOthersentry.delete(0,"end")
    labelInsuranceentry.delete(0,"end")
    labelTaxesentry.delete(0,"end")
    labelVacationentry.delete(0,"end")
    labelOtherentry.delete(0,"end")
    labelmPayentry.delete(0,"end")
    labelmOthersentry.delete(0,"end")
    labelaGiftsentry.delete(0,"end")
    titlemEx1["text"]=""
    titleaEx1["text"]=""
    titlemI1["text"]=""
    titlebudget1["text"]=""
    titlebudget1["bg"]="lightpink"


def calculate():
    EF = labelEFentry.get()
    Investments = labelInvestmentsentry.get()
    Retirement = labelRetiremententry.get()
    Food = labelFoodentry.get()
    Cloth = labelClothentry.get()
    Shelter = labelShelterentry.get()
    Household = labelHouseholdentry.get()
    Transport = labelTransportentry.get()
    Health = labelHealthentry.get()
    Personal = labelPersonalentry.get()
    Others = labelOthersentry.get()
    Insurance = labelInsuranceentry.get()
    Taxes = labelTaxesentry.get()
    Vacation = labelVacationentry.get()
    Other = labelOtherentry.get()
    mPay = labelmPayentry.get()
    mOthers = labelmOthersentry.get()
    aGifts = labelaGiftsentry.get()
    try:
        EF = int(EF)
        Investments = int(Investments)
        Retirement = int(Retirement)
        Food = int(Food)
        Cloth = int(Cloth)
        Shelter = int(Shelter)
        Household = int(Household)
        Transport = int(Transport)
        Health = int(Health)
        Personal = int(Personal)
        Others = int(Others)
        Insurance = int(Insurance)
        Taxes = int(Taxes)
        Vacation = int(Vacation)
        Other = int(Other)
        mPay = int(mPay)
        mOthers = int(mOthers)
        aGifts = int(aGifts)
        savings = EF+Investments+Retirement
        mexpenses = Food+Cloth+Shelter+Household+Transport+Health+Personal+Others
        aexpenses = Insurance+Taxes+Vacation+Other
        mIncome = mPay+mOthers+aGifts
        titlemEx1["text"]=str(mexpenses)
        titleaEx1["text"]=str(aexpenses/12)
        titlemI1["text"]=str(mIncome)
        budget=mIncome-mexpenses
        if budget>=savings:
            titlebudget1["text"]=str(budget)
            titlebudget1["bg"]="green"
        else:
            titlebudget1["text"]=str(budget)
            titlebudget1["bg"]="red"
        
    except:
        messagebox.showwarning("Warning","All Values must be an Integer")

    
    



#monthly savings
titlemSavings = tkinter.Label(root,text="Monthly Savings",bg="lightpink")
titlemSavings.config(width="40")
titlemSavings.grid(row=0,column=0)

labelEF = tkinter.Label(root,text="Emergency Funds")
labelEF.config(width="40")
labelEF.grid(row=1,column=0)

labelEFentry = tkinter.Entry(root,bg="white")
labelEFentry.grid(row=1,column=1)

labelInvestments = tkinter.Label(root,text="Investments")
labelInvestments.config(width="40")
labelInvestments.grid(row=2,column=0)

labelInvestmentsentry = tkinter.Entry(root,bg="white")
labelInvestmentsentry.grid(row=2,column=1)

labelRetirement = tkinter.Label(root,text="Retirement")
labelRetirement.config(width="40")
labelRetirement.grid(row=3,column=0)

labelRetiremententry = tkinter.Entry(root,bg="white")
labelRetiremententry.grid(row=3,column=1)

titleblank = tkinter.Label(root,text="",bg="lightyellow")
titleblank.config(width="3")
titleblank.grid(row=0,column=3)

#monthly expenses
titlemExpenses = tkinter.Label(root,text="Monthly Expenses",bg="lightpink")
titlemExpenses.config(width="40")
titlemExpenses.grid(row=4,column=0)

labelFood = tkinter.Label(root,text="Food")
labelFood.config(width="40")
labelFood.grid(row=5,column=0)

labelFoodentry = tkinter.Entry(root,bg="white")
labelFoodentry.grid(row=5,column=1)

labelCloth = tkinter.Label(root,text="Clothing")
labelCloth.config(width="40")
labelCloth.grid(row=6,column=0)

labelClothentry = tkinter.Entry(root,bg="white")
labelClothentry.grid(row=6,column=1)

labelShelter = tkinter.Label(root,text="Shelter")
labelShelter.config(width="40")
labelShelter.grid(row=7,column=0)

labelShelterentry = tkinter.Entry(root,bg="white")
labelShelterentry.grid(row=7,column=1)

labelHousehold = tkinter.Label(root,text="Household")
labelHousehold.config(width="40")
labelHousehold.grid(row=8,column=0)

labelHouseholdentry = tkinter.Entry(root,bg="white")
labelHouseholdentry.grid(row=8,column=1)

labelTransport = tkinter.Label(root,text="Transport")
labelTransport.config(width="40")
labelTransport.grid(row=9,column=0)

labelTransportentry = tkinter.Entry(root,bg="white")
labelTransportentry.grid(row=9,column=1)

labelHealth = tkinter.Label(root,text="Health")
labelHealth.config(width="40")
labelHealth.grid(row=10,column=0)

labelHealthentry = tkinter.Entry(root,bg="white")
labelHealthentry.grid(row=10,column=1)

labelPersonal = tkinter.Label(root,text="Personal")
labelPersonal.config(width="40")
labelPersonal.grid(row=11,column=0)

labelPersonalentry = tkinter.Entry(root,bg="white")
labelPersonalentry.grid(row=11,column=1)

labelOthers = tkinter.Label(root,text="Miscellaneous")
labelOthers.config(width="40")
labelOthers.grid(row=12,column=0)

labelOthersentry = tkinter.Entry(root,bg="white")
labelOthersentry.grid(row=12,column=1)

#annual expenses
titleaExpenses = tkinter.Label(root,text="Annual Expenses",bg="lightpink")
titleaExpenses.config(width="40")
titleaExpenses.grid(row=13,column=0)

labelInsurance = tkinter.Label(root,text="Insurance")
labelInsurance.config(width="40")
labelInsurance.grid(row=14,column=0)

labelInsuranceentry = tkinter.Entry(root,bg="white")
labelInsuranceentry.grid(row=14,column=1)

labelTaxes = tkinter.Label(root,text="Taxes")
labelTaxes.config(width="40")
labelTaxes.grid(row=15,column=0)

labelTaxesentry = tkinter.Entry(root,bg="white")
labelTaxesentry.grid(row=15,column=1)

labelVacation = tkinter.Label(root,text="Vacation")
labelVacation.config(width="40")
labelVacation.grid(row=16,column=0)

labelVacationentry = tkinter.Entry(root,bg="white")
labelVacationentry.grid(row=16,column=1)

labelOther = tkinter.Label(root,text="Other")
labelOther.config(width="40")
labelOther.grid(row=17,column=0)

labelOtherentry = tkinter.Entry(root,bg="white")
labelOtherentry.grid(row=17,column=1)


#income
titleIncome = tkinter.Label(root,text="Income",bg="lightpink")
titleIncome.config(width="40")
titleIncome.grid(row=18,column=0)

labelmPay = tkinter.Label(root,text="Monthly Pay")
labelmPay.config(width="40")
labelmPay.grid(row=19,column=0)

labelmPayentry = tkinter.Entry(root,bg="white")
labelmPayentry.grid(row=19,column=1)

labelmOthers = tkinter.Label(root,text="Monthly Other")
labelmOthers.config(width="40")
labelmOthers.grid(row=20,column=0)

labelmOthersentry = tkinter.Entry(root,bg="white")
labelmOthersentry.grid(row=20,column=1)

labelaGifts = tkinter.Label(root,text="Annual Gifts")
labelaGifts.config(width="40")
labelaGifts.grid(row=21,column=0)

labelaGiftsentry = tkinter.Entry(root,bg="white")
labelaGiftsentry.grid(row=21,column=1)

#Summary

titleSummary = tkinter.Label(root,text="Total Summary",bg="lightpink")
titleSummary.config(width="40")
titleSummary.grid(row=0,column=4)

titlemEx = tkinter.Label(root,text="Monthly Expenses",bg="lightyellow")
titlemEx.grid(row=2,column=4)

titlemEx1 = tkinter.Label(root,text="",bg="lightyellow")
titlemEx1.grid(row=3,column=4)

titleaEx = tkinter.Label(root,text="Annual Expenses(per month division)",bg="lightyellow")
titleaEx.grid(row=5,column=4)

titleaEx1 = tkinter.Label(root,text="",bg="lightyellow")
titleaEx1.grid(row=6,column=4)

titlemI = tkinter.Label(root,text="Monthly Income",bg="lightyellow")
titlemI.grid(row=8,column=4)

titlemI1 = tkinter.Label(root,text="",bg="lightyellow")
titlemI1.grid(row=9,column=4)

titlebudget = tkinter.Label(root,text="Budget",bg="lightpink")
titlebudget.grid(row=11,column=4)

titlebudget1 = tkinter.Label(root,text="",bg="lightpink",fg="white")
titlebudget1.grid(row=12,column=4)


#Buttons
btn_reset= tkinter.Button(root, text="Reset", fg="white", bg="black", command=reset)
btn_reset.config(width=15)
btn_reset.grid(row=22,column=0)

btn_calc= tkinter.Button(root, text="Calculate", fg="black", bg="lightgray", command=calculate)
btn_calc.config(width=15)
btn_calc.grid(row=22,column=1)

btn_exit= tkinter.Button(root, text="Exit", fg="white", bg="red", command=exit)
btn_exit.config(width=15)
btn_exit.grid(row=22,column=4)

root.mainloop()
