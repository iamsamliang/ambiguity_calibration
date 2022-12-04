import json
import random

def main():
  # select years we want to choose (must be between 2010 and 2020 inclusive)
  first_year = '2010'
  second_year = '2020'

  # populate these two arrays with only questions that have answers in these years
  first_year_arr = []
  second_year_arr = []

  # Opening JSON file
  f = open('time_questions.json')
    
  # returns JSON object as an array of dictionaries
  data = json.load(f)

  # Closing file
  f.close()
    
  # Iterating through the array of dictionaries and selecting questions from our years of interest
  for question in data:
    if question['date'] == first_year:
      first_year_arr.append(question)
    elif question['date'] == second_year:
      second_year_arr.append(question)

  # for i in range(5):
  #   print(first_year_arr[i])
  #   print()
  
  # print()

  # for i in range(5):
  #   print(second_year_arr[i])
  #   print()

  
  # sample num_questions of questions from these two arrays
  num_questions = 5
  
  first_year_questions = random.sample(first_year_arr, k=num_questions)
  second_year_questions = random.sample(second_year_arr, k=num_questions)

  print(first_year_questions)
  print()
  print(second_year_questions)
  print()

  # only take the query and answer fields
  for i in range(len(first_year_questions)):
    new_dict = {}
    new_dict['query'] = first_year_questions[i]['query']
    new_dict['answer'] = first_year_questions[i]['answer']
    first_year_questions[i] = new_dict

    new_dict = {}
    new_dict['query'] = second_year_questions[i]['query']
    new_dict['answer'] = second_year_questions[i]['answer']
    second_year_questions[i] = new_dict

  combined_questions = [*first_year_questions, *second_year_questions]
  print(combined_questions)

  # Serializing json
  json_object = json.dumps(combined_questions, indent=4)
  
  # Writing to sample.json
  with open(f"{first_year}_{second_year}.json", "w") as outfile:
      outfile.write(json_object)

if __name__ == '__main__':
    main()