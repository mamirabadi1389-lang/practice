class Hello:
    def __init__(self, hello, goodbye, enter):
        self.hello = hello
        self.goodbye = goodbye
        self.enter = enter

    def __str__(self):
        return f"man grok hastam {self.hello}. agrt ba man kare nadare man beram {self.goodbye}"

    # اضافه کردن قابلیت ماشین حساب
    def hesaban(self, num1, num2):
        # اینجا یک عملیات ساده جمع قرار دادیم
        num1 = float(input("عدد اول را وارد کنید: "))
        operator = input("عملگر را وارد کنید (+, -, *, /, **, %): ")
        num2 = float(input("عدد دوم را وارد کنید: "))
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "خطا: تقسیم بر صفر مجاز نیست"
        elif operator == "**":
            result = num1 ** num2
        elif operator == "%":
            result = num1 % num2
        else:
            result = "خطا: عملگر نامعتبر است"
        
        print("نتیجه:", result)

        return f"نتیجه محاسبات شما برابر است با: {result}"
    def hook ():
        pass
# مقداردهی درست (باید ۳ پارامتر مطابق __init__ داده شود)
a = Hello("salam", "khodahafez", "ورود")

# چاپ رشته کلاس
print(a)

# استفاده از ماشین حساب
print(a.hesaban(10, 20))
