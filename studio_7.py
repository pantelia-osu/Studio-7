import csv

class Participant:
    def __init__(self, age, industry, salary, currency, country, experience, education):
        self.age = age
        self.industry = industry
        self.salary = salary
        self.currency = currency
        self.country = country
        self.experience = experience
        self.education = education

class AverageSalary:
    def __init__(self, key, average, participant_count):
        self.key = key
        self.average = average
        self.participant_count = participant_count

def main():
    print("Studio 7")
    print("-------------------------------------------------------------------------------------------------------")
    rows = read_csv_file("survey.csv")
    participants = parse_csv(rows)
    print_statements(participants)

def print_statements(participants):
    statements = {
        "Number of participants": len(participants),
        "Top 5 industries": top_5_industries_by_salary(participants),
        "Average Salary By Age": avg_salary_by_age(participants),
        "Average Salary By Highest Education Level": avg_salary_by_education(participants),
        "Average Salary By Years of Experience": avg_salary_by_experience(participants)
    }
    for key, value in statements.items():
        print(key, ":", value)
        print("------------------------------------------------------------------------------------------------------- \n")

def parse_csv(data):
    participants = []
    """headers = data[0]"""
    for row in data[1:]:
        age = row[1]
        industry = row[2]
        salary = int(row[5].replace(",",""))
        currency = row[7]
        country = row[10]
        experience = row[13]
        education = row[15]
        if currency == "USD":
            participants.append(Participant(age, industry, salary, currency, country, experience, education))
    return participants

def read_csv_file(file_name):
    rows = []
    with open(file_name, "r", newline='') as csvfile:
        data = list(csv.reader(csvfile))
        for row in data:
            rows.append(row)
    return rows

def top_5_industries_by_salary(participants):
    industry_salary = {}
    industries = group_by_attribute(participants, "industry")
    for industry, participants in industries.items():
        total_salary = sum([participant.salary for participant in participants])
        industry_salary[industry] = int(total_salary / len(participants))
    top_5_industries = sorted(industry_salary.items(), key=lambda x: x[1], reverse=True)[:5]
    return top_5_industries

def avg_salary_by_age(participants):
    age_salary = {}
    ages = group_by_attribute(participants, "age")
    for age, participants in ages.items():
        total_salary = sum([participant.salary for participant in participants])
        age_salary[age] = int(total_salary / len(participants))
    age_salary = sorted(age_salary.items(), key=lambda x: x[1], reverse=True)[:5]
    return age_salary

def avg_salary_by_education(participants):
    education_salary = {}
    educations = group_by_attribute(participants, "education")
    for education, participants in educations.items():
        total_salary = sum([participant.salary for participant in participants])
        education_salary[education] = int(total_salary / len(participants))
    education_salary = sorted(education_salary.items(), key=lambda x: x[1], reverse=True)[:5]
    return education_salary

def avg_salary_by_experience(participants):
    experience_salary = {}
    experiences = group_by_attribute(participants, "experience")
    for experience, participants in experiences.items():
        total_salary = sum([participant.salary for participant in participants])
        experience_salary[experience] = int(total_salary / len(participants))
    experience_salary = sorted(experience_salary.items(), key=lambda x: x[1], reverse=True)[:5]
    return experience_salary

def group_by_attribute(objects, property):
    groups = {}
    
    for obj in objects:
        value = getattr(obj, property)
        if value in groups:
            groups[value].append(obj)
        else:
            groups[value] = [obj]

    return groups

def get_value_by_property(object_list, property):
    values = []
    for obj in object_list:
        values.append(getattr(obj, property))
    return list(set(values))

def filter_by_value(object_list, property, value):
    return list(filter(lambda x: getattr(x, property) == value, object_list))

if __name__ == "__main__":
    main()