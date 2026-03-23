# Tailored Immersive Environments: Advancing Neurodivergent Support Through Virtual Reality - arXiv

# Tailored Immersive Environments: Advancing Neurodivergent Support Through Virtual Reality 

 Elia Moscoso-Thompson  Katia Lupinetti  Irene Capasso  Fabrizio Ravicchio  Brigida Bonino  Franca Giannini  Andrea Canessa  Silvio Sabatini  Lucia Ferlino  Chiara Malagoli 

Abstract

Every day life tasks can present significant challenges for neurodivergent individuals, particularly those with Autism Spectrum Disorders (ASD) who are characterized by specific sensitivities. This contribution describes a virtual reality system that allows neurodivergent individuals to experience everyday situations in order to practice and implement strategies for overcoming their daily challenges. The key strength of the proposed system is the automatic personalization of the virtual environment, based on both the individual’s abilities and their specific training needs. The proposed method has been evaluated on four synthetic user profiles, also proposing a metric able to evaluate the variance of the features within the same difficulty level. The results show that the method can produce a significant number of scenarios for the various difficulty levels. Furthermore, within the same difficulty, there is a wide variance of the non-constrained features for the specific profile.

## I  Introduction  

Urbanisation is advancing at an unprecedented rate, expanding city boundaries and population density. While new technologies make modern cities more connected, the resulting sensory and social complexity can hinder mobility, especially for people whose perceptual and cognitive processing differs from the neurotypical norm. Among them, neurodivergent individuals are disproportionately affected: atypical sensory filtering and heightened cognitive load interact with dense traffic, unpredictable pedestrian behaviour, and highly stimulating architecture, turning apparently mundane journeys into demanding problem-solving tasks.

Current therapeutic approaches for individuals with neurodivergent conditions are often unable to integrate the sensory and perceptual complexity of real-world environments. This limits the real-life applicability and generalization of coping strategies learned during therapy. From the research point of view, new technologies are employed to improve current approaches and virtual reality applications has been investigated deeply  [[1](https://arxiv.org/html/2601.08652v1#bib.bib28)] . Didehbani et al.  [[3](https://arxiv.org/html/2601.08652v1#bib.bib30)]  proposed a VR training through a desktop application that allows trainees to test their abilities on 10 prefabricated modules, interacting with virtual avatars. Frolli et al.  [[2](https://arxiv.org/html/2601.08652v1#bib.bib31)]  proposed an emotional training in virtual reality and compared it with traditional emotional training performed individually with a therapist. Saiano et al.  [[6](https://arxiv.org/html/2601.08652v1#bib.bib32)]  proved that a gesture-based “natural” interface combined with a desktop virtual environment can safely train adults on the autism spectrum to follow paths and cross streets. These systems, although innovative from the technological point of view, are limited considering their personalization capabilities; indeed few adjustments are possible (not even in all the systems), and the tuning of the configurations strongly depends on the therapist. This limitation strongly prevents the possibility of tailoring the training to each individual’s specific needs.

To address this gap, we design and implement EASE VR—Empowering Accessible Social Engagement in Virtual Reality, a system for creating ecologically valid, personalized virtual environments that reflect the user’s sensory and cognitive challenges. Through EASE VR, users can face complex crossing situations in a controlled and safe environment. Each scenario can be adjusted to the sensory and cognitive needs of the individual through a therapist-facing personalization interface.

## II  The EASE VR system  

The EASE VR system includes distinct training scenarios conceptualized and designed to simulate real-world situations that can be perceived as particularly challenging for neurodivergent individuals. Each scenario allows participants to complete specific tasks that assess their ability in living different places of the city, and among the scenarios that EASE VR proposes, the  Urban Crosswalk Scenario  is particularly relevant, and in this work, we focus on this scenario and its personalization. It is designed to reproduce, through hyperrealistic graphics and high visual realism  [[7](https://arxiv.org/html/2601.08652v1#bib.bib26)] , everyday life challenges for individuals with ASD connected to the extreme complexity of the city environment linked to sensory overstimulation  [[5](https://arxiv.org/html/2601.08652v1#bib.bib2)]  and the unpredictable dynamic of multiple situations and conditions (e.g., lights and weather conditions, noises, the number of people and vehicles, people’s interaction, different waiting times, detours, unexpected behavior of others, vehicles passing despite stop signs, strikes, etc.). Consequently, this scenario integrates specific challenges such as managing waiting times, visuo-spatially orienting in the virtual environment while correctly assessing the situation, and extracting or requesting information to correctly manage the specific presented challenge, while dealing with sensory and social stimulation, providing integrated ecologically comparable physical and social functional mediators to support the ecological generalization of developed behaviors in real life  [[8](https://arxiv.org/html/2601.08652v1#bib.bib23)] .

In this scenario, participants must successfully cross a virtual street while adhering to standard pedestrian rules to reach a specific place. Depending on the difficulty level, the pedestrian crossing length and difficulty environmental conditions, such as time of day (day/night), weather (rain/sun), traffic density, and pedestrian flow can be modified and personalized according to the user’s characteristics. Unexpected events, such as a vehicle running a red light or an ambulance passing through the intersection with sirens on, are introduced to experience and evaluate the participant’s ability to react to unforeseen situations, observing the ability of participants to manage the cognitive load and overall sensory stimulation. An increasing complexity results in progressive modifications to the above-mentioned environmental parameters within the scenario, accompanied by alterations in stimulus presentation that respond dynamically to participant’s performance and needs. This tailoring is individually calibrated both in terms of cognitive characteristics and level of functioning of each participant. The customization is facilitated through an external graphic user interface, which enables to adjust every element in the scenario. This means that the maximum difficulty threshold exhibits inter-individual variation, reflective each participant’s sensory sensitivities and cognitive profile.

## III  Personalization method and experiment setup  

According to the Urban Crosswalk Scenario design, the proposed personalization method enables the generation of VR environments, where the configurable features are:

•  

Type of crossing : short, long, double;

•  

Light setting : day, night;

•  

Rain : sunny, rain;

•  

Presence of pedestrians : low, medium, high flow;

•  

Presence of vehicles : low, medium, high flow;

•  

Sudden sound distractors : presence or absence of church bells, helicopters, car red lights;

•  

Background noise : volume noise of ambulances, baby crying, and dogs’ barking;

•  

Type of traffic light : absence, standard, presence of push-button and/or countdown, or broken.

Fig [1](https://arxiv.org/html/2601.08652v1#S3.F1) presents three examples of pedestrian crossing scenarios obtained by combining various parameters previously described.

(a) Simple urban scenario   (b) Rainy urban scenario   (c) Night urban scenario   Figure 1:  Examples of different training scenarios.  

A value is assigned to each feature state, sorting them based on the expected level of difficulty. Without practical knowledge of the actual perceived difficulty, the values are equally spaced on the range  [ 0 , 1 ] [0,1] . For example,  Type of crossing  can assume the value  1 / 3 1/3  (short),  2 / 3 2/3  (long),  1 1  (double).

To help formalize our analysis, we use  ϕ i \phi_{i}  to represent a feature. Moreover, to encode the different difficulty perceptions based on the user capabilities, we add a weight  ω j \omega_{j}  to each feature, ranging from  1 1  to  5 5 . We group some features based on the aspect we impact in the scenario, and we assign them the same weights (e.g., all  Sudden sound distractors  have the same weight). For an overview of the notation used in this work, we refer to Table [I](https://arxiv.org/html/2601.08652v1#S3.T1).

TABLE I:  Overview of the notation used in the analysis to describe a scenario.   Feature name   Feature values   Cognitive skill   \rowcolor [HTML]EFEFEF  ϕ 1 \phi_{1}   Type of crossing   {1/3 (short), 2/3 (long), 1 (double)}   ω 1 \omega_{1}   Visuospatial awareness   ϕ 2 \phi_{2}   Night time   {0 (day time), 1 (night time)}   ϕ 3 \phi_{3}   Rain   {0 (sunny), 1 (rainy)}   ω 2 \omega_{2}   Pattern vision   \rowcolor [HTML]EFEFEF  ϕ 4 \phi_{4}   Presence of pedestrians   {0 (no one), 1/2 (some people), 1 (many people)}   ω 3 \omega_{3}   Social factor   ϕ 5 \phi_{5}   Presence of vehicles   {0 (no cars), 1/2 (some cars), 1 (many cars)}   ω 4 \omega_{4}   Hazard factor   \rowcolor [HTML]EFEFEF  ϕ 6 \phi_{6}   ssd: church bell   {0 (no sound), 1 (sound activated)}   \cellcolor [HTML]EFEFEF   \cellcolor [HTML]EFEFEF   \rowcolor [HTML]EFEFEF  ϕ 7 \phi_{7}   ssd: helicopter   {0 (no sound), 1 (sound activated)   \cellcolor [HTML]EFEFEF   \cellcolor [HTML]EFEFEF   \rowcolor [HTML]EFEFEF  ϕ 8 \phi_{8}   ssd: car wating red lights   {0 (no sound), 1 (sound activated)   \cellcolor [HTML]EFEFEF ω 5 \omega_{5}   \cellcolor [HTML]EFEFEFSudden Sound perception   ϕ 9 \phi_{9}   bn: ambulance   {0, 1/3, 2/3, 1}*   ϕ 10 \phi_{10}   bn: baby crying   {0, 1/3, 2/3, 1}*   ϕ 11 \phi_{11}   bn: dogs barking   {0, 1/3, 2/3, 1}*   ω 6 \omega_{6}   Tolerance to noise   \rowcolor [HTML]EFEFEF  ϕ 12 \phi_{12}   Traffic light   {1/6, 1/3, 1/2, 2/3, 5/6, 1}**   ω 7 \omega_{7}   Rule complexity and hazard factor  

( ∗ ) (*) : background noises (bn) varies from  0  to  1 1 . Given the exploratory nature of this work, we only assume there are four possible volume setups: mute, low, medium, and high.  ( ∗ ∗ ) (**) : we considered the following traffic light (TL) states: (1) no traffic light, (2) presence of a basic TL, (3) TL with a pedestrian button, (4) TL with a visible countdown timer, (5) TL with both button and timer, and (6) broken or malfunctioning TL.

The personalization algorithm follows a four-step process to generate training scenarios aligned with user-specific profiles.

•  

First, all possible combinations of scenario parameters are computed by systematically varying the values of each feature. This exhaustive enumeration ensures full coverage of the scenario space.

•  

Second, for each combination, a difficulty score is computed using a linear weighted sum:

D score = ∑ ( i , j ) ω i  ϕ j , D_{\text{score}}=\sum_{(i,j)}\omega_{i}\phi_{j},   (1)  

for opportune  ( i , j ) (i,j)  combinations based on what reported in Table [I](https://arxiv.org/html/2601.08652v1#S3.T1). This difficulty score allows for ranking each scenario difficulty according to the specific profile (encoded through the weights). Notice that, if a feature can be disabled on a scenario (e.g., a sound), we also add  0  to the possible values, so that the weight does not influence to the score if feature is not present.

•  

Third, profile-specific constraints are applied to filter out combinations that contain features deemed unsuitable or non-beneficial for the given user (e.g., suppressing loud stimuli for sound-sensitive users at the beginning of the training), or selecting exactly those elements that are relevant for the traing (e.g. a certain type of traffic light).

•  

Finally, the resulting difficulty scores are normalized to the  [ 0 , 1 ] [0,1]  interval, enabling consistent comparisons across profiles and scenario sets.

This entire process exhibits linear computational complexity with respect to the number of combinations, making the method both scalable and computationally efficient for real-time scenario generation. Here, the idea is that for a fixed difficulty score  D s  c  o  r  e D_{score} , the generated scenarios vary in content while preserving the overall training challenge level. This enables the construction of training paths that are ecologically diverse but therapeutically consistent. In addition, to ensure clinical relevance, constraints are applied after scenario generation. These constraints enforce the presence (or exclusion) of specific features depending on the user profile.

### III-A   Score discretization and consistent difficulty  

Given the number of features and the range of values each feature can assume, the number of different scores varies significantly. To support the exploratory purpose of this work, we group similar scores with an adaptive discretization approach. In other words, we discretize the scenarios  D s  c  o  r  e D_{score}  so that two different scores have significant differences in feature setup and value. Specifically, we define the larger possible score increase, denote it  δ \delta , and use it to segment the score range  [ 0 , 1 ] [0,1] . A more formal definition of  δ \delta  is as follow:

δ = max  ( ω i  ϕ i ) , ∀ i , \delta=\text{max}(\omega_{i}\phi_{i}),\qquad\forall i,   (2)  

reminding that  ϕ i \phi_{i}  and  ω i \omega_{i}  represent the feature value and related weight, respectively. This choice ensures that each score interval includes meaningful features variation.

Then, we cluster scenarios with similar  D score D_{\text{score}} , referring to these cluster as scenarios sets with consistent difficulty ( C  D score CD_{\text{score}} ). These are computed as follows:

C  D score = r  o  u  n  d  ( D score δ ) − 1 , CD_{\text{score}}=round\left(\frac{D_{\text{score}}}{\delta}\right)^{-1},   (3)  

where  r  o  u  n  d  ( ⋅ ) round(\cdot)  denotes the round operator. Taking the reciprocal of the ratio helps normalize  C  D score CD_{\text{score}}  values to lie between  0  and  1 1 .

Profile 1: Sound hypersensitive (290304 out of 331776 profile specific scenarios - 87.5%)   All scenarios   Profile specific scenarios   Figure 2:  Profile 3 scenarios analysis. Left: the distribution of scenarios (the y-axis is in logarithmic scale). Right: the related variance in features values.   Profile 2: Excessively focused attention on a detail   Vol  < 33 % <33\%  (9216 out of 331776 profile specific scenarios - 2.7%)   33 % < 33\%<  Vol  < 66 <66  (31104 out of 331776 profile specific scenarios - 9.4%)   66 % < 66\%<  Vol  < 100 % <100\%  (73728 out of 331776 profile specific scenarios - 22.2%)   All scenarios   Profile specific scenarios   Figure 3:  Profile 2 scenarios analysis. Left: the distribution of scenarios (the y-axis is in logarithmic scale). Right: the related variance in features values.   Profile 3: Social anxiety (16384 out of 331776 profile specific scenarios - 4.9%)   Profile 4: Intermittent attention (147456 out of 331776 profile specific scenarios - 44.4%)   All scenarios   Profile specific scenarios   Figure 4:  Profile 3 and 4 scenarios analysis. Left: the distribution of scenarios (the y-axis is in logarithmic scale). Right: the related variance in features values.  

## IV  Evaluation objectives and adopted metrics  

This tool aims to help therapists by facilitating the design and control of the training scenario. This ambitious goal requires multiple tests and validations (see Section [VI](https://arxiv.org/html/2601.08652v1#S6)). In this work, we focus on validating the personalization approach, demonstrating that:

1.  

The proposed scenario personalization is able to define distinct sets of scenarios according to different user profiles;

2.  

Given a  C  D s  c  o  r  e CD_{score}  and the feature constraints of a certain user profile, the proposed scenario personalization is able to define scenarios that differ significantly, enabling ecological training environments.

To this aim, we have defined four different synthetic user profiles describing their difficulties in the general task of crossing a street, which will represent the feature constraints. These profiles have the mere scope to allow us to simulate some of the characteristics that may occur in the ASD spectrum, but by any means must be considered neither exhaustive of the broad spectrum of individual differences, resulting in extremely complex profiles, nor as accurate of the overall spectrum of difficulties that may be registered in the described situation.

The weights utilized in this study are determined based on our expertise with respect to the target user perception, and the actual values are empirically derived. These weights are detailed in Table [II](https://arxiv.org/html/2601.08652v1#S4.T2). Point 1) of the evaluation also aims to verify qualitatively that the weighted scenarios are meaningful for the specific user profile. The following are the syntactic user profile descriptions.

•  

Profile 1: Sound hypersensitive  - Unable to filter out loud noises, may freeze at the sound of the ambulance siren, may decide not to cross even when it is safe, as the sensory overload may obstruct the person’s ability to assess and execute the necessary procedures to complete the action.  Relevant challenges : Presence of loud noises.

•  

Profile 2: Excessively focused attention on a detail  - Focuses on the duration of the timer, unable to shift attention from that detail, does not cross, even though the situation is safe, because the timer dynamic locks the person’s attentional resources and makes it difficult to be able to assess if the amount of time shown is enough to cross safely.  Relevant challenges : Presence of the traffic light with a functioning timer, different lengths of crossings, and volumes of noise must be incremental.

•  

Profile 3: Social anxiety  - Avoids interaction with other pedestrians, crosses only during less crowded moments, possibly even if less safe.  Relevant challenges : Presence of people, medium or long crossing, lack of safety.

•  

Profile 4: Intermittent attention  - Registers difficulties in maintaining the focus of attention for an extended amount of time, consequently registers difficulties in processing the complexity of the presented situation, in organizing the stimuli, and deciding on whether it is safe to cross or not.  Relevant challenges : Longer crossing, medium presence of vehicles.

TABLE II:  Mapping of personalization weights to scenario parameters and cognitive skill   ω 1 \omega_{1}   ω 2 \omega_{2}   ω 3 \omega_{3}   ω 4 \omega_{4}   ω 5 \omega_{5}   ω 6 \omega_{6}   ω 7 \omega_{7}   \rowcolor [HTML]EFEFEF Profile 1   2   2   2   2   5   5   3   Profile 2   3   1   3   3   3   3   3   \rowcolor [HTML]EFEFEF Profile 3   2   2   5   5   2   2   2   Profile 4   5   2   2   3   2   2   2  

### IV-A   Measuring feature variation in scenarios with consistent difficulty  

We aim to examine how the features vary between scenarios of consistent difficulty. In particular, we are interested in determining whether each feature within a set of scenarios exhibits an even distribution of its possible values. For example, if a feature  ϕ i \phi_{i}  can take values in  { 0 , 0.5 , 1 } \{0,0.5,1\}  and we consider a set of scenarios, we define it as varying “as much as possible” if each value appears exactly  1 3 \frac{1}{3}  of the time. In other words, based on this approach, for each feature  ϕ i \phi_{i}  that can assume  p 1 , … , p n p_{1},\dots,p_{n}  values there is an ideal distribution  ϕ i ¯ \overline{\phi_{i}}  for its values, which is defined as:

ℙ  ( ϕ i ¯ = p k ) = 1 / n ∀ i = 1 , … , n . \mathbb{P}(\overline{\phi_{i}}=p_{k})=1/n\qquad\forall i=1,\dots,n.   (4)  

Thus, we use the divergence between the probability distributions to estimate the variation of features and ensure the generation of distinct scenarios. To do so, we exploit the Jensen–Shannon divergence[[4](https://arxiv.org/html/2601.08652v1#bib.bib1)]  ( J  S  D JSD  for short) between the distribution of a set of scenarios with consistent difficulty and its ideal distribution.

To ease the visualization of this analysis, to estimate the variance  𝒱 \mathcal{V}  of a feature  ϕ i \phi_{i}  we use the following formula:

𝒱  ( ϕ i ) = 1 − J  D  S  ( ϕ i , ϕ i ¯ ) . \mathcal{V}(\phi_{i})=1-JDS(\phi_{i},\overline{\phi_{i}}).   (5)  

Since  J  D  S JDS  varies between  0  and  1 1 ,  𝒱 \mathcal{V}  value is higher if the divergence is low (or rather, the distribution of  ϕ i \phi_{i}  values is good), and vice-versa.

By computing  𝒱 \mathcal{V}  for each feature across all score values, we visualize the results using a multi-line graph (one per feature), providing a quantitative and intuitive representation of the features variation across different scores. In an ideal scenario, each lines would remain constant at value of  1 1 , indicating perfect uniformity in value distribution.

## V  Results  

For Profile 1, the challenge of the presence of loud noise has been translated in selecting scenarios including at least one feature ssd, i.e. church bell, helicopter or car waiting red lights. Fig.[2](https://arxiv.org/html/2601.08652v1#S3.F2) illustrates the number of relevant scenarios clustered for the difficulty level. We can observe that once the constrain is applied, the number of scenarios does not decrease significantly for each  C  D s  c  o  r  e CD_{score} , indeed 87,5% of the scenarios includes the challenges considered relevant for profile 1. Considering how the features vary between scenarios of consistent difficulty, we can observe that  𝒱  ( ϕ i ) \mathcal{V}(\phi_{i})   ∀ i \forall i  rapidly approach a plateau near 1, indicating scenario diversity. Notice that among the axis key constrained features are not reported since they are fixed, and considering their variance is not meaningful for this evaluation.

For profile 2, feature constrain are represent by the presence of the traffic light with a functioning timer and the different lengths of crossings. The fact that volumes of noise must be incremental among the difficulty level has been translated into setting volumes under a certain threshold (minor of 33 %) for easy level, among a certain range for middle range (grather that 33% and minor than 66%), and over a certain threshold for high level (greater that 66%), then the results are depicted in Fig.[3](https://arxiv.org/html/2601.08652v1#S3.F3) with three different charts, for easy/medium/high level of the training. Despite this heavy restriction (for instance, only 2,7% of the scenarios have the requirements for the easy level), we can positively observe that an important number of scenarios is present in each  C  D s  c  o  r  e CD_{score} . This is also true for the middle and the high level. Also in this case, we can observe that the free feature tends to 1, ensuring a wide variety of scenarios within the same  C  D s  c  o  r  e CD_{score} .

Profile 3 is characterized by many constraints. Indeed, scenario features require setting many people, medium or long crossing, and the lack of safety has been translated into a high number of vehicles and broken traffic light. To respect all the constraints, we can observe in Fig.[4](https://arxiv.org/html/2601.08652v1#S3.F4)(top) that the minimum selectable  C  D s  c  o  r  e CD_{score}  is 0.3. This evaluation is essential in our future work to set properly easy/middle/high level according to the  C  D s  c  o  r  e CD_{score}  tailored for each person.

Finally, scenarios of profile 4 must present longer crossing and a medium presence of vehicles. Also in this case, we can observe in Fig.[4](https://arxiv.org/html/2601.08652v1#S3.F4)(bottom) that after  C  D s  c  o  r  e = 0.5 CD_{score}=0.5  all the consistent difficulty score include a significative number of scenarios with a peak in the medium consistent difficulty score. The scenarios variance again shows a balanced use of all features value, converging towards 1 after  C  D s  c  o  r  e = 1 CD_{score}=1 .

Generally, across all profiles, we can observe that below a certain threshold (around 0,2) the variation of the feature is present ( 𝒱  ( ϕ i ) = 0 \mathcal{V}(\phi_{i})=0   ∀ i \forall i ). The value of the threshold depends on the user profile, i.e., on the weights used to define the scenarios. The same observation is valid for the tails of the scenarios’ variance plots, indicating that over a certain  C  D s  c  o  r  e CD_{score}  (the specific threshold depends on the users’ profile), the variation of the features is not ensured and then the proposed scenarios are quite similar among them.

## VI  Conclusions and future works  

In this work, we proposed a method for personalizing urban training scenarios specifically tailored for neurodivergent individuals, allowing them to experience scenarios of increasing complexity. The proposed approach was evaluated using four synthetic user profiles, accompanied by a metric designed to assess the variance of a single feature within scenarios of equivalent difficulty levels.

The results demonstrate that our method effectively generates a substantial number of diverse scenarios across multiple difficulty levels. Importantly, significant variance is maintained within the same difficulty category, particularly for features that were not explicitly constrained by the specific user profile. This indicates the method’s capability to deliver a rich spectrum of scenarios, offering valuable variability while maintaining targeted constraints.

Although preliminary, this research represents a critical step towards establishing precise thresholds for easy, medium, and difficult scenario classifications based on derived difficulty scores. Future work will involve collaboration with neurodivergent participants to accurately profile their responses and perceptions of difficulty. One possible approach is to propose a limited series of scenarios with significant differences to both the therapists and the users, collecting feedback on calibration. Subsequently, similar scenarios  C  D s  c  o  r  e CD_{score}  will be presented to validate the consistency of the challenge at a fixed difficulty level. This feedback will also help to refine the assessment criteria, in order to achieve the ambitious goal of developing a semi-supervised personalization mechanism.

Moreover, different evaluation metrics beyond variance will be explored, searching for metrics that highlight scenarios diversity under different perspectives. Finally, computational complexity is not expected to pose a major challenge in this study, but are conducting stress tests using “large” feature spaces to better understand the scalability and limitations.

## References

[1]   J. Abich IV, J. Parker, J. S. Murphy, and M. Eudy  (2021)   A review of the evidence for training effectiveness with virtual reality technology .  Virtual Reality   25  ( 4 ),   pp. 919–933 .  Cited by: [§I](https://arxiv.org/html/2601.08652v1#S1.p2.1). 

[2]   A. Frolli, G. Savarese, F. Di Carmine, A. Bosco, E. Saviano, A. Rega, M. Carotenuto, and M. C. Ricci  (2022)   Children on the autism spectrum and the use of virtual reality for supporting social skills .  Children   9  ( 2 ),   pp. 181 .  Cited by: [§I](https://arxiv.org/html/2601.08652v1#S1.p2.1). 

[3]   F. Ke, J. Moon, and Z. Sokolikj  (2022)   Virtual reality–based social skills training for children with autism spectrum disorder .  Journal of Special Education Technology   37  ( 1 ),   pp. 49–62 .  Cited by: [§I](https://arxiv.org/html/2601.08652v1#S1.p2.1). 

[4]   J. Lin  (1991-01)   Divergence measures based on the shannon entropy .  IEEE Transactions on Information Theory   37  ( 1 ),   pp. 145–151 .  External Links: [Document](https://dx.doi.org/10.1109/18.61115),  ISSN 0018-9448 , [Link](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=61115)Cited by: [§ IV-A](https://arxiv.org/html/2601.08652v1#S4.SS1.p1.7). 

[5]   I. Miller, B. Wiederhold, C. Miller, and M. Wiederhold  (2020-01)   Virtual reality air travel training with children on the autism spectrum: a preliminary report .  Cyberpsychol Behav Soc Netw   23  ( 1 ),   pp. 10–15 .  External Links: [Document](https://dx.doi.org/10.1089/cyber.2019.0093), [Link](doi:10.1089/cyber.2019.0093),  ISSN 2152-2723   Cited by: [§II](https://arxiv.org/html/2601.08652v1#S2.p1.1). 

[6]   M. Saiano, L. Pellegrino, M. Casadio, S. Summa, E. Garbarino, V. Rossi, D. Dall’Agata, and V. Sanguineti  (2015)   Natural interfaces and virtual environments for the acquisition of street crossing and path following skills in adults with autism spectrum disorders: a feasibility study .  Journal of neuroengineering and rehabilitation   12 ,   pp. 1–13 .  Cited by: [§I](https://arxiv.org/html/2601.08652v1#S1.p2.1). 

[7]   M. Slater, P. Khanna, J. Mortensen, and I. Yu  (2009-05)   Visual realism enhances realistic response in an immersive virtual environment .  IEEE computer graphics and applications   29 ,   pp. 76–84 .  External Links: [Document](https://dx.doi.org/10.1109/MCG.2009.55)Cited by: [§II](https://arxiv.org/html/2601.08652v1#S2.p1.1). 

[8]   T. Stokes and P. Osnes  (2016-09)   An operant pursuit of generalization – republished article .  Behavior Therapy   47 ,   pp. 720–732 .  External Links: [Document](https://dx.doi.org/10.1016/j.beth.2016.08.012)Cited by: [§II](https://arxiv.org/html/2601.08652v1#S2.p1.1). 