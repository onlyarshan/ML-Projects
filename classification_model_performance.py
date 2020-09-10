# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:28:42 2020

@author: Admin
"""

def model_performance(model):
    model.fit(X_train,y_train)
    RF_training_labels = model.predict(X_train)
    RF_test_labels = model.predict(X_test)
    Training_accuracy = model.score(X_train, y_train, sample_weight=None)
    Test_accuracy = model.score(X_test, y_test, sample_weight=None)
    F1_score_train = f1_score(y_train, RF_training_labels, average = 'weighted')
    F1_score_test = f1_score(y_test, RF_test_labels, average = 'weighted')
    Recall_train = recall_score(y_train, RF_training_labels, average = 'weighted') 
    Recall_test  = recall_score(y_test, RF_test_labels, average = 'weighted') 
    Precision_train = precision_score(y_train, RF_training_labels, average = 'weighted')
    Precision_test = precision_score(y_test, RF_test_labels, average = 'weighted')
    accuracy_score
    rf_cm_tr = confusion_matrix(y_train, RF_training_labels)
    rf_cm_te = confusion_matrix(y_test, RF_test_labels)
    print("Training_accuracy - ", Training_accuracy)
    print("Test_accuracy - ", Test_accuracy)
    print("F1_score_train - ", F1_score_train)
    print("F1_score_test - ", F1_score_test)
    print("Recall_train - ", Recall_train)
    print("Recall_test - ", Recall_test)
    print("Precision_train - ", Precision_train)
    print("Precision_test - ", Precision_test)
    
    #Confusion Matrix
    class_names=[0,1] # name  of classes
    fig, ax = plt.subplots()
    tick_marks = np.arange(len(class_names))
    plt.xticks(tick_marks, class_names)
    plt.yticks(tick_marks, class_names)
    # create heatmap
    sns.heatmap(pd.DataFrame(rf_cm_te), annot=True, cmap="YlGnBu" ,fmt='g')
    ax.xaxis.set_label_position("top")
    plt.tight_layout()
    plt.title('Test Confusion matrix', y=1.1)
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')
    

    return RF_training_labels, RF_test_labels 