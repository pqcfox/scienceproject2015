import os
import random
import shutil

# Split corpus into training and test sets

corpus = "corpus"
test_set = "test_set"
train_set = "train_set"
train_size = 15

print "Removing old test/train sets..."
 
for s in [test_set, train_set]:
    try:
        shutil.rmtree(s)
    except OSError:
        pass
    os.mkdir(s)
    os.chmod(s, 0o775)


print "Splitting corpus..."

classes = sorted([ os.path.join(corpus, f) for f in os.listdir(corpus) if os.path.isdir(os.path.join(corpus, f)) ])
for c in classes:
    images = [ os.path.join(c, f) for f in os.listdir(c) ]
    train = random.sample(images, train_size)
    test = [ f for f in images if not f in train ]
    base = os.path.basename(c) 
    os.mkdir(os.path.join(train_set, base))
    os.mkdir(os.path.join(test_set, base))
 
    for f in train:
        shutil.copy(f, os.path.join(train_set, base))

    for f in test:
        shutil.copy(f, os.path.join(test_set, base))
 
