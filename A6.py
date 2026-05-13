class InformationExpertSystem:

    def __init__(self):
        self.rules = {
            "data": {
                "storage": "Use databases or cloud storage.",
                "backup": "Maintain regular backups."
            },
            "security": {
                "low": "Use password protection.",
                "high": "Use encryption and multi-factor authentication."
            },
            "search": {
                "fast": "Use indexing techniques.",
                "accurate": "Use optimized search algorithms."
            }
        }

    def infer(self, category, need):
        return self.rules.get(category, {}).get(need, "No rule found.")

    def run(self):
        print(" Information Management Expert System")
        while True:
            category = input("Enter category (data/security/search or exit): ").lower()
            if category == "exit":
                break
            need = input("Enter requirement: ").lower()
            print("Advice:", self.infer(category, need))


system = InformationExpertSystem()
system.run()








class HospitalExpertSystem:

    def __init__(self):
        # Knowledge Base (rules)
        self.rules = {
            "fever": {
                "mild": "Take paracetamol and rest.",
                "high": "Consult a doctor immediately."
            },
            "cough": {
                "dry": "Take cough syrup.",
                "severe": "Visit a physician."
            },
            "injury": {
                "minor": "Apply first aid.",
                "major": "Go to emergency ward."
            }
        }

    # Inference Engine
    def diagnose(self, symptom, severity):
        if symptom in self.rules:
            if severity in self.rules[symptom]:
                return self.rules[symptom][severity]
            else:
                return "Severity not recognized."
        else:
            return "Symptom not recognized."

    # User Interface
    def run(self):
        print("🏥 Hospital Expert System")
        print("Type 'exit' to quit\n")

        while True:
            symptom = input("Enter symptom (fever/cough/injury): ").lower()

            if symptom == "exit":
                print("Thank you!")
                break

            severity = input("Enter severity (mild/high/dry/severe/minor/major): ").lower()

            result = self.diagnose(symptom, severity)
            print("Diagnosis:", result)
            print()


# Run system
system = HospitalExpertSystem()
system.run()



class HelpDeskExpertSystem:

    def __init__(self):
        self.rules = {
            "login": {
                "error": "Reset your password.",
                "locked": "Contact admin to unlock account."
            },
            "network": {
                "slow": "Check bandwidth usage.",
                "down": "Restart router or contact ISP."
            },
            "software": {
                "crash": "Reinstall the software.",
                "update": "Install latest updates."
            }
        }

    def infer(self, issue, type_):
        return self.rules.get(issue, {}).get(type_, "No solution found.")

    def run(self):
        print("💻 Help Desk Expert System")
        while True:
            issue = input("Enter issue (login/network/software or exit): ").lower()
            if issue == "exit":
                break
            type_ = input("Enter problem type: ").lower()
            print("Solution:", self.infer(issue, type_))


system = HelpDeskExpertSystem()
system.run()








class EmployeeExpertSystem:

    def __init__(self):
        self.rules = {
            "attendance": {
                "good": "Eligible for bonus.",
                "poor": "Needs improvement."
            },
            "performance": {
                "high": "Promotion recommended.",
                "medium": "Maintain performance.",
                "low": "Training required."
            },
            "behavior": {
                "excellent": "Leadership role suitable.",
                "average": "Improve communication.",
                "bad": "Counseling required."
            }
        }

    def evaluate(self, factor, level):
        return self.rules.get(factor, {}).get(level, "No evaluation found.")

    def run(self):
        print("👨‍💼 Employee Evaluation Expert System")
        while True:
            factor = input("Enter factor (attendance/performance/behavior or exit): ").lower()
            if factor == "exit":
                break
            level = input("Enter level: ").lower()
            print("Result:", self.evaluate(factor, level))


system = EmployeeExpertSystem()
system.run()








class StockExpertSystem:

    def __init__(self):
        self.rules = {
            "trend": {
                "bullish": "Buy stocks.",
                "bearish": "Sell stocks.",
                "stable": "Hold position."
            },
            "risk": {
                "high": "Invest in volatile stocks.",
                "low": "Invest in safe assets."
            },
            "time": {
                "short": "Prefer intraday trading.",
                "long": "Go for long-term investment."
            }
        }

    def advise(self, factor, value):
        return self.rules.get(factor, {}).get(value, "No advice found.")

    def run(self):
        print("📈 Stock Market Expert System")
        while True:
            factor = input("Enter factor (trend/risk/time or exit): ").lower()
            if factor == "exit":
                break
            value = input("Enter value: ").lower()
            print("Advice:", self.advise(factor, value))


system = StockExpertSystem()
system.run()