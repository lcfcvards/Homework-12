import pickle

data = [{'Anna': 90, 'Ivan': 50}, {'Petr': 52, 'Vasiliy': 641}, {'Andrey': 6, 'Roman': 84}, {'Marina': 48, 'Olga': 28}]

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('data.pickle', 'rb') as f:
    data_new = pickle.load(f)
