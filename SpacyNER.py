import spacy
import plac
import random
from pathlib import Path
import time

@plac.annotations(
    model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_iter=("Number of training iterations", "option", "n", int))
def main(model=None, output_dir=None, n_iter=20):
    """Load the model, set up the pipeline and train the entity recognizer."""
    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank('en')  # create blank Language class
        print("Created blank 'en' model")

    # create the built-in pipeline components and add them to the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner, last=True)
    # otherwise, get it so we can add labels
    else:
        ner = nlp.get_pipe('ner')

    # add labels
    for _, annotations in TRAIN_DATA:
        for ent in annotations.get('entities'):
            ner.add_label(ent[2])

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()
        for itn in range(n_iter):
            #random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in TRAIN_DATA:
                nlp.update(
                    [text],  # batch of texts
                    [annotations],  # batch of annotations
                    drop=0.5,  # dropout - make it harder to memorise data
                    sgd=optimizer,  # callable to update weights
                    losses=losses)
            print(losses)

    # test the trained model

    count = 0
    for text,_ in TEST_DATA:
        doc = nlp(text)
        #print(text)
                
        #print('Entities', [(ent.text, ent.label_) for ent in doc.ents])
        #print('Tokens', [(t.text, t.ent_type_, t.ent_iob) for t in doc])
        for ent in doc.ents:
            prediction.append(ent.text+'@'+ent.label_)



if __name__ == '__main__':
    time_start = time.time()
    train_data = open("/Users/alfred/PycharmProjects/NER/conll03/eng.train", "r")
    test_data = open("/Users/alfred/PycharmProjects/NER/conll03/eng.testb", "r")

    s_train = ' '
    s_test = ' '
    data_train = []
    data_test = []
    list_train = []
    list_test = []
    input_train = []
    input_test = []
    prediction = []
    output_list = []

    for token in train_data:
        word = token.split(' ')[0]
        entity = token.split(' ')[-1]
        #print(output)
        if word != '\n':

            s_train = s_train + word + ' '
            start = s_train.index(word)
            end = s_train.index(word) + len(word)
            recog = entity.strip()
            # print(j)
            data_train.append((start, end, recog))

        else:
            input_train.append((s_train, {'entities': data_train}))
            # print(s)
            s_train = ''
            data_train = []
            # print(input)


    for token in test_data:
        word = token.split(' ')[0]
        entity = token.split(' ')[-1]
        if word != '\n':
            output_list.append(token.strip())
            s_test = s_test + word + ' '
            start = s_test.index(word)
            end = s_test.index(word) + len(word)
            recog = entity.strip()
            # print(j)
            data_test.append((start, end, recog))

        else:
            input_test.append((s_test, {'entities': data_test}))
            # print(s)
            s_test = ''
            data_test = []
            # print(input)

    txt2 = open('outputlist.txt', 'w')
    for i in range(len(output_list)):
        # print(output_list)
        # output_list[i] = output_list[i] + " " + prediction[i]
        # print(output_list[i])
        print(output_list[i], file=txt2)
    txt2.close()

    demo_train = []
    for i in input_train:
        # print(i)
        demo_train.append(i)
    print(demo_train)
    demo_test = []

    for i in input_test:
        # print(i)
        demo_test.append(i)

    TRAIN_DATA = demo_train
    TEST_DATA = demo_test

    #print(TRAIN_DATA[0])



    plac.call(main)
    print(len(prediction),len(output_list))
    #print(prediction)

    txt = open('result1.txt','w')

    i=0
    j=0
    while i<len(output_list) and j<len(output_list):
         if (output_list[i]).split(" ")[0] == (prediction[j]).split("@")[0]:
            output_list[i] = output_list[i] + " " + (prediction[j]).split("@")[-1]
            print(output_list[i], file=txt)
            i =i+1
            j =j+1

         if (output_list[i]).split(" ")[0] != (prediction[j]).split("@")[0]:
            output_list[i] = output_list[i] + " O"
            print(output_list[i], file=txt)
            i=i+1
            j=j

    txt.close()

    txt1 = open('output1.txt','w')

    for i in range(len(prediction)):
        print(prediction[i], file=txt1)

    txt1.close()

    print(len(prediction))
    print(i)
    print(j)
    time_end = time.time()
    execution_time = time_end-time_start

    print(execution_time)
    #print(output_list)
    #print(prediction)
