import keyword
import random
import time
import turtle

def decrypt_clue(text):
    answer1=[]
    for i in dic:
        word = i
        if word in text:
            answer1.append(word)
    return(answer1)
text= "ThereareyouIandletlistintgameJupiterlinedefblindasyieldassertbreakclasscontinueexceptfinallyforfromglobalimportnonlocalpassraisereturntrywhilewithandorasassertbreakclasscontinuedefdelelifelseexceptexecfinallyforfromglobalifimportinislambdnonlocalnotorpassprintraisereprreturnsupertrywhilewithyieldTrueFalseNoneasyncawaitmatchcasenonelocaloverrideprivatesealedstaticmethodvolatileabstractenumintfloatdoublebyteboolcharstructvectorlistdictionaryqueuestackinterfacenulltrycatchfinallythrowthrowsimplementsextendspublicprotectedprivatefinalstaticvoidmainStringargsSystemoutprintlnnewMapSetGetAddRemoveClearIsEmptySizeContainsKeyContainsValueKeyValuePairsForEachDoWhileSwitchCaseDefaultbreakcontinueiteratoriterablecollectionsframeworksynchronizedtransientvolatilestrictfpbitwiselogicalshiftcompoundassignmenttypeinferencegenericswildcardstypeerasurereflectionproxydecoratorfactorysingletonprototypebuildercompositeadapterbridgechainofresponsibilitycommandstateobservermementointerpreteriteratorvisitorstrategytemplatemethodflyweightmediatorproxymultithreadingconcurrencyasynchronousprogrammingeventdrivenarchitecturefunctionalprogrammingimmutables...quantumcomputingqubitsentanglementsuperpositionquantumalgorithmsShorsGroverquantumcryptographyquantumteleportationartificialintelligenceAIoptimizationalgorithmsgraphtheorytraversalsearchalgorithmsdepthfirstsearchbreadthfirstsearchAstaralgorithmgeneticalgorithmssimulatedannealingparticlewarmoptimizationantcolonyoptimizationmachinelearningdeeplearningunsupervisedlearningreinforcementlearningneuralnetworksconvolutionalneuralnetworksrecurrentneuralnetworkslongshorttermmemorynetworksgenerativeadversar...blockchaintechnologydistributedledgerconsensusalgorithmsproofOfWorkproofOfStakeByzantineFaultTolerancepeer-to-peerP2PnetworkscryptographyhashfunctionsasymmetricencryptionpublickeyinfrastructurePKIdigitalcertificatesdigital signaturesmartcontractsdecentralizedapplicationsDAppsEthereumplatformSolidityprogramminglanguageWeb3technologyNFTsnon-fungibletokensDeFidecentralizedfinancedecentralizedexchangesDEXsstablecoinscryptocurrencyminingstakingyieldfarmingliquiditypoolsoraclesDAOsdecentralizedautonomousorganizati"

def slove_puzzles(puzzles):
    true_word_list =[]
    false_word_list =[]
    None_word_list =[]
    for i in puzzles:
        if bool(i)==True:
            true_word_list.append(i)
        elif bool(i)==False:
            false_word_list.append(i)
        elif bool(i)==None:
            None_word_list.append(i)


    print("true list is:")        
    for x in true_word_list:
        print("\n",x)
    print("false list is:")
    for x in false_word_list:
        print("\n",x)
    print("none list is:")
    for x in None_word_list:
        print("\n",x)
    return(true_word_list)

def calculate_magic_numbers():
    x = random.randint(0,15)
    return(x)
def exam_numbers(x):
    global correct_answer
    global wrong_answer
    binarynum=0
    i=1
    y=x
    while y>0:
        re = y%2
        binarynum += re*i
        y= (y) // 2
        i*=10
    print("pls convert dec to bin\n")
    print(binarynum)
    answer = int(input())
    if answer == x :
        correct_answer=correct_answer+1
    else:
        wrong_answer = wrong_answer+1
def check_pass(backpack):
    filter_len=[]
    for username, password in backpack:
        lenght=len(password)
        if lenght>=8:
            filter_len.append((username,password))
    filter_cap=[]
    for username, password in filter_len:
        if any(char.isupper() for char in password) and any (char.islower() for char in password):
            filter_cap.append((username,password))
    global filter_punctuation
    for username, password in filter_len:
        if any(char in "!@#$%^&*-_=+?"for char in password):
            filter_punctuation.append((username,password))
    return(filter_punctuation)
def unlock_vault(answer1,answer2,answer3):
    finalanswer=answer1+answer2+answer3
    return(finalanswer)



puzzles = [
    'ali',
    1233,
    0,
    "",
    [],
    {},
    'False',
    '0',
    'None',
    None,
    -1,
    [1, 2, 3],
    {'key': 'value'},
    True,
    ' ',
    '[]',
    '[1, 2, 3]',
    '{}',
    "{'a': 1}",
    'True',
    'ali',
    '1234',
    1,
    0.1,
    -0.1,
    True,
    ' ',
    '[]',
    '[1, 2, 3]',
    '{}',
    "{'a': 1}",
    'True',
    'ali',
    '1234',
    1,
    0.1,
    -0.1,
    True,
    ' ',
    '[]',
    '[1, 2, 3]',
    '{}',
    "{'a': 1}",
    'True'
]
dic=keyword.kwlist
text= "ThereareyouIandletlistintgameJupiterlinedefblindasyieldassertbreakclasscontinueexceptfinallyforfromglobalimportnonlocalpassraisereturntrywhilewithandorasassertbreakclasscontinuedefdelelifelseexceptexecfinallyforfromglobalifimportinislambdnonlocalnotorpassprintraisereprreturnsupertrywhilewithyieldTrueFalseNoneasyncawaitmatchcasenonelocaloverrideprivatesealedstaticmethodvolatileabstractenumintfloatdoublebyteboolcharstructvectorlistdictionaryqueuestackinterfacenulltrycatchfinallythrowthrowsimplementsextendspublicprotectedprivatefinalstaticvoidmainStringargsSystemoutprintlnnewMapSetGetAddRemoveClearIsEmptySizeContainsKeyContainsValueKeyValuePairsForEachDoWhileSwitchCaseDefaultbreakcontinueiteratoriterablecollectionsframeworksynchronizedtransientvolatilestrictfpbitwiselogicalshiftcompoundassignmenttypeinferencegenericswildcardstypeerasurereflectionproxydecoratorfactorysingletonprototypebuildercompositeadapterbridgechainofresponsibilitycommandstateobservermementointerpreteriteratorvisitorstrategytemplatemethodflyweightmediatorproxymultithreadingconcurrencyasynchronousprogrammingeventdrivenarchitecturefunctionalprogrammingimmutables...quantumcomputingqubitsentanglementsuperpositionquantumalgorithmsShorsGroverquantumcryptographyquantumteleportationartificialintelligenceAIoptimizationalgorithmsgraphtheorytraversalsearchalgorithmsdepthfirstsearchbreadthfirstsearchAstaralgorithmgeneticalgorithmssimulatedannealingparticlewarmoptimizationantcolonyoptimizationmachinelearningdeeplearningunsupervisedlearningreinforcementlearningneuralnetworksconvolutionalneuralnetworksrecurrentneuralnetworkslongshorttermmemorynetworksgenerativeadversar...blockchaintechnologydistributedledgerconsensusalgorithmsproofOfWorkproofOfStakeByzantineFaultTolerancepeer-to-peerP2PnetworkscryptographyhashfunctionsasymmetricencryptionpublickeyinfrastructurePKIdigitalcertificatesdigital signaturesmartcontractsdecentralizedapplicationsDAppsEthereumplatformSolidityprogramminglanguageWeb3technologyNFTsnon-fungibletokensDeFidecentralizedfinancedecentralizedexchangesDEXsstablecoinscryptocurrencyminingstakingyieldfarmingliquiditypoolsoraclesDAOsdecentralizedautonomousorganizati"
decrypt_clue(text)
print(decrypt_clue(text))
answer1=decrypt_clue(text)[0][0]
slove_puzzles(puzzles)
answer2=(slove_puzzles(puzzles)[0][0])
correct_answer=0
wrong_answer=0
start_time=time.time()
while (time.time() - start_time) <20:
    calculate_magic_numbers()
    x=calculate_magic_numbers()
    exam_numbers(x)
print("number of corrrect answer:",correct_answer)
print("number of wrong answer:",wrong_answer)
backpack=[]
filter_punctuation=[]
while True:
    username=(input("pls enter your username or q for finish:"))
    if username=="q":
        break
    else :
        password=(input("pls enter your pass: "))
        backpack.append((username,password))
check_pass(backpack)
print(filter_punctuation)
answer3=filter_punctuation[0][0][0]


wn = turtle.Screen()
wn.title("amiram")
amiram = turtle.Turtle()
amiram.goto(0, 0)  


amiram.left(90)
amiram.forward(100)
amiram.backward(100)
amiram.left(90)
amiram.forward(30)
amiram.right(90)
amiram.forward(100)
amiram.penup()
amiram.goto(-50,0)
amiram.pendown()
amiram.forward(20)
amiram.backward(20)
amiram.left(90)
amiram.forward(40)
amiram.penup()
amiram.goto(-60,30)
amiram.pendown()
amiram.circle(5)
amiram.penup()
amiram.goto(-80,30)
amiram.pendown()
amiram.circle(5)
amiram.penup()
amiram.goto(-90,0)
amiram.pendown()
amiram.left(90)
for i in range(3):
    amiram.forward(20)
    amiram.right(24)
amiram.penup()
amiram.goto(-110,0)
amiram.pendown()
amiram.right(16)
amiram.right(45)
amiram.forward(40)
amiram.left(90)
amiram.forward(20)
amiram.penup()
amiram.goto(-110,0)
amiram.pendown()
amiram.right(45)
amiram.forward(50)
amiram.left(24)
amiram.forward(20)
for i in range(3):
    amiram.left(48)
    amiram.forward(25)
for i in range(3):
    amiram.right(48)
    amiram.forward(25)
for i in range(4):
    amiram.forward(40)
    amiram.right(48)
amiram.penup()
amiram.goto(-130,-30)
amiram.pendown()
amiram.circle(5)
wn.mainloop()

unlock_vault(answer1,answer2,answer3)
final_answer=unlock_vault(answer1,answer2,answer3)
print("final answer is =",final_answer)