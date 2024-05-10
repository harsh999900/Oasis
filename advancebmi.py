# Advanced Version: Graphical BMI Calculator with Data Storage and Visualization

import tkinter as tk
import sqlite3
import matplotlib.pyplot as plt

class BMIApp:
    def __init__(self, master):
        self.master = master
        self.master.title("BMI Calculator")
        
        self.label_weight = tk.Label(master, text="Weight (kg):")
        self.label_weight.grid(row=0, column=0)
        self.entry_weight = tk.Entry(master)
        self.entry_weight.grid(row=0, column=1)
        
        self.label_height = tk.Label(master, text="Height (m):")
        self.label_height.grid(row=1, column=0)
        self.entry_height = tk.Entry(master)
        self.entry_height.grid(row=1, column=1)
        
        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, columnspan=2)
        
        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=3, columnspan=2)
        
        # Initialize database
        self.conn = sqlite3.connect("bmi_data.db")
        self.create_table()
    
    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS bmi_records
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           weight REAL,
                           height REAL,
                           bmi REAL)''')
        self.conn.commit()
    
    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())
            
            if weight <= 0 or height <= 0:
                self.result_label.config(text="Please enter valid weight and height values.")
                return
            
            bmi = weight / (height ** 2)
            category = self.categorize_bmi(bmi)
            self.result_label.config(text=f"BMI: {bmi:.2f}, Category: {category}")
            
            # Store data in database
            cursor = self.conn.cursor()
            cursor.execute('''INSERT INTO bmi_records (weight, height, bmi) VALUES (?, ?, ?)''', (weight, height, bmi))
            self.conn.commit()
            
            # Visualize data
            self.visualize_data()
            
        except ValueError:
            self.result_label.config(text="Please enter valid numeric values.")
    
    def categorize_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    
    def visualize_data(self):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT weight, height, bmi FROM bmi_records''')
        records = cursor.fetchall()
        
        weights = [record[0] for record in records]
        heights = [record[1] for record in records]
        bmis = [record[2] for record in records]
        
        plt.scatter(weights, bmis)
        plt.xlabel("Weight (kg)")
        plt.ylabel("BMI")
        plt.title("Weight vs BMI")
        plt.show()

def main():
    root = tk.Tk()
    app = BMIApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
