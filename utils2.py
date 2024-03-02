import pickle
import numpy as np
import config
import json



def get_predicted_charges(age,gender,bmi,children,smoker,region):

    print('age,gender,bmi,children,smoker,region',age,gender,bmi,children,smoker,region)
    model_file_path = config.MODEL_FILE_PATH

    with open(model_file_path, 'rb') as f:
        model = pickle.load(f)

    with open(config.COLUMN_DATA_JSON, 'r') as f:
        col_data = json.load(f)

    col_names = model.feature_names_in_


    region_index = np.where(col_names == 'region_'+ region)[0][0]
    # print("region_index",region_index)

    gender = col_data['gender'][gender]
    smoker = col_data['smoker'][smoker]

    test_array = np.zeros((1,model.n_features_in_))
    test_array[0,0] = age
    test_array[0,1] = gender
    test_array[0,2] = bmi
    test_array[0,3] = children
    test_array[0,4] = smoker
    test_array[0,region_index] = 1

    predicted_price = model.predict(test_array)
    print("predicted_price :",predicted_price)

    return predicted_price
