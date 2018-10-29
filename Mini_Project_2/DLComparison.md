############################################################### 
Comparison between ResNet50 and MobileNet (by John Neal for Mini Project 2 for EC 601 at Boston University)
###############################################################

Primary Source for ResNet50 knowledge: https://arxiv.org/abs/1512.03385

Primary Source for MobileNet knowledge: https://arxiv.org/pdf/1704.04861.pdf

This comparison will take the form of a Q&A dialogue:

# When were the papers on ResNet50 and MobileNet published?

ResNet50's paper "Deep Residual Learning for Image Recognition" was published on 5/10/16. whereas MobileNet's 
"MobileNets: Efﬁcient Convolutional Neural Networks for Mobile Vision Applications" was published on 4/17/17.
This means the paper on MobileNet is 2 years newer than the paper on ResNet50, which is considerable.

# What is the most obvious difference between the ResNet50 and MobileNet models?

Besides being newer, MobileNet focuses on the size and speed of the convolutional neural network.
It's name hints at mobile applications. ResNet50, on the other hand, were designed to address a degradation of training accuracy
problem which was noticed as more and more layers were being stacked onto the CNN. While I did not dive too deep into the math,
my limited understanding seems to be that ResNet50 was designed to address a bottleneck with respect to accuracy, whereas MobileNet
was designed to focus on a relatively ignored aspect of CNNs for the purpose of real-life application.

# What are the applications of ResNet50 and MobileNet?

The title of ResNet50's article suggests its use is for Image Recognition. This may be a result of
using the ImageNet dataset. It is not apparent to me whether it's unique approach with Residual Learning
is particularly for the application for Image Recognition. The concept of Residual Learning seems abrstact enough
to be applied to other applications.

On the other hand, MobileNet's article makes its applications very explicit. Geolocalization, facial recognition, and object detection
all have devoted sections in their article. MobileNet aims to be a model for real life applications that require fast and accurate calculations
with little space.

# Further questions?

As I am entirely new to the world of machine learning, it seems somewhat dishonest to present any "knowledge" that I may have gained without
a thorough acknowledgement of my own ignorance.

Specifically for ResNet50, I would like to understand further how the "shorcut" connections spoken of in the article
are its key to avoiding the degrdation of training accuracy. The quote I am refering to is: "Based on the above plain network, we
insert shortcut connections (Fig. 3, right) which turn the network into its counterpart residual version."

I'd also like to understand this quote on mapping, which seems to convey how this residual learning model is unique:
"So rather than expect stacked layers to approximate H(x), we explicitly let these layers approximate a residual function
F(x) := H(x) − x. The original function thus becomes F(x)+x. Although both forms should be able to asymptotically
approximate the desired functions (as hypothesized), the ease of learning might be different."


### Notes on each article ####################################################################################################################


### ResNet50

# What is Residual Learning?

-- "We explicitly reformulate the layers as learning
residual functions with reference to the layer inputs, instead
of learning unreferenced functions. We provide comprehensive
empirical evidence showing that these residual
networks are easier to optimize, and can gain accuracy from
considerably increased depth."

-- "The depth of representations is of central importance
for many visual recognition tasks."

-- "An ensemble of these residual nets achieves 3.57% error
on the ImageNet test set."

-- "the “levels” of features can be enriched
by the number of stacked layers (depth)."

-- "Driven by the significance of depth, a question arises: Is
learning better networks as easy as stacking more layers?"

-- "When deeper networks are able to start converging, a
degradation problem has been exposed: with the network
depth increasing, accuracy gets saturated (which might be
unsurprising) and then degrades rapidly"

-- "In this paper, we address the degradation problem by
introducing a deep residual learning framework"

-- "Instead
of hoping each few stacked layers directly fit a
desired underlying mapping, we explicitly let these layers
fit a residual mapping."

-- "We show that: 1) Our extremely deep residual nets
are easy to optimize, but the counterpart “plain” nets (that
simply stack layers) exhibit higher training error when the
depth increases; 2) Our deep residual nets can easily enjoy
accuracy gains from greatly increased depth, producing results
substantially better than previous networks."

# What is a residual mapping?

-- "We adopt residual learning to every few stacked layers."

-- "But we will
show by experiments that the identity mapping is sufficient
for addressing the degradation problem and is economical,
and thus Ws is only used when matching dimensions."

-- "So
rather than expect stacked layers to approximate H(x), we
explicitly let these layers approximate a residual function
F(x) := H(x) − x. The original function thus becomes
F(x)+x. Although both forms should be able to asymptotically
approximate the desired functions (as hypothesized),
the ease of learning might be different."

-- "Based on the above plain network, we
insert shortcut connections (Fig. 3, right) which turn the
network into its counterpart residual version."

-- "Next we evaluate 18-layer and 34-
layer residual nets (ResNets). The baseline architectures
are the same as the above plain nets, expect that a shortcut
connection is added to each pair of 3×3 filters as in Fig. 3
(right)."

-- "But there are still open problems on such aggressively
deep models. The testing result of this 1202-layer network
is worse than that of our 110-layer network, although both
training data 07+12 07++12
test data VOC 07 test VOC 12 test
VGG-16 73.2 70.4
ResNet-101 76.4 73.8
Table 7. Object detection mAP (%) on the PASCAL VOC
2007/2012 test sets using baseline Faster R-CNN. See also Table
10 and 11 for better results.
metric mAP@.5 mAP@[.5, .95]
VGG-16 41.5 21.2
ResNet-101 48.4 27.2
Table 8. Object detection mAP (%) on the COCO validation set
using baseline Faster R-CNN. See also Table 9 for better results.
have similar training error. We argue that this is because of
overfitting."

### MobileNets

# Why MobileNets?

-- "We present a class of efficient models called MobileNets
for mobile and embedded vision applications."

-- "In many real world applications such as robotics,
self-driving car and augmented reality, the recognition tasks
need to be carried out in a timely fashion on a computationally
limited platform."

-- "The general trend
has been to make deeper and more complicated networks
in order to achieve higher accuracy [27, 31, 29, 8].  However,
these advances to improve accuracy are not necessarily
making networks more efficient with respect to size and
speed."

# What sets MobileNets apart?

-- "uses depthwise
separable convolutions to build light weight deep
neural networks."

-- "We introduce two simple global hyperparameters
that efficiently trade off between latency and
accuracy. These hyper-parameters allow the model builder
to choose the right sized model for their application based
on the constraints of the problem."

-- "present extensive
experiments on resource and accuracy tradeoffs"

-- "We then demonstrate the effectiveness
of MobileNets across a wide range of applications and
use cases including object detection, finegrain classification,
face attributes and large scale geo-localization."

-- "Many different approaches can be generally
categorized into either compressing pretrained networks or
training small networks directly. This paper proposes a
class of network architectures that allows a model developer
to specifically choose a small network that matches
the resource restrictions (latency, size) for their application."

-- "MobileNet models were trained in TensorFlow [1] using
RMSprop [33] with asynchronous gradient descent similar
to Inception V3 [31]"

# MobileNet Network Architecture

-- "MobileNets are built primarily from depthwise separable
convolutions initially introduced in [26] and subsequently
used in Inception models [13] to reduce the computation in
the first few layers."

-- "In this section we first describe the core layers that MobileNet
is built on which are depthwise separable filters.
We then describe the MobileNet network structure and conclude
with descriptions of the two model shrinking hyperparameters
width multiplier and resolution multiplier."

-- "The standard convolution operation has the effect of filtering
features based on the convolutional kernels and combining
features in order to produce a new representation . . . The filtering and combination steps can be split into two
steps via the use of factorized convolutions called depthwise separable
convolutions for substantial reduction in computational
cost."

-- "The MobileNet structure is built on depthwise separable
convolutions as mentioned in the previous section except for
the first layer which is a full convolution"

# Width Multiplier: Hyperparameter 1

-- "many times a specific use case or
application may require the model to be smaller and faster.
In order to construct these smaller and less computationally
expensive models we introduce a very simple parameter α
called width multiplier. The role of the width multiplier α is
to thin a network uniformly at each layer."

# Resolution Multiplier: Hyperparameter 2

-- "The second hyper-parameter to reduce the computational
cost of a neural network is a resolution multiplier ρ. We 
apply this to the input image and the internal representation of
every layer is subsequently reduced by the same multiplier."

# Useful for:

-- Geolocalization
-- Facial recognition
-- Object detection