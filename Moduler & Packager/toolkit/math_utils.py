import math

def factorial(n):
    return math.factorial(int(n))

def compound_interest(principal, rate_percent, time_years, compounds_per_year=1):
    r = rate_percent / 100
    amount = principal * (1 + r / compounds_per_year) ** (compounds_per_year * time_years)
    return round(amount, 2)

def trigonometry(angle_deg):
    rad = math.radians(angle_deg)
    return {"sin": round(math.sin(rad), 3), "cos": round(math.cos(rad), 3), "tan": round(math.tan(rad), 3)}

def area_of_circle(radius):
    return round(math.pi * radius ** 2, 2)

def area_of_rectangle(length, width):
    return round(length * width, 2)
