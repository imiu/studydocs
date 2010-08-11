# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    inputFile = open(filename)
    subject_dict = {}
    for line in inputFile:
        name, value, work = line.split(',')
        value = int(value)
        work = int(work.strip())
        subject_dict[name] = (value, work)
    return subject_dict

    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    if val1 > val2:
        return 1
    else:
        return -1

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    if work1 < work2:
        return 1
    else:
        return -1

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    if float(val1) / work1 > float(val2) / work2:
        return 1
    else:
        return -1

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    adv_subjects = {}
    work_cnt = 0
    tmp_subj = [(v, w, n) for n, (v, w) in subjects.iteritems()]
    for v, w, n in sorted(tmp_subj, cmp=comparator, reverse=True):
        if (work_cnt + w < maxWork):
            adv_subjects[n] = (v, w)
            work_cnt += w
        else:
            break
    return adv_subjects

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    filename = 'subjects.txt'
    max_work = 5
    subject_dict = loadSubjects(filename)
    start_time = time.time()
    adv_subjects = bruteForceAdvisor(subject_dict, max_work)
    end_time = time.time()
    total_time = end_time - start_time
    printSubjects(adv_subjects)
    print "Total time with max_work = %d is %0.4f seconds" %(max_work, total_time)

# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance
#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            dpAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0, {})
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def dpAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                                subset, subsetValue, subsetWork, memo):
    global numCalls
    numCalls += 1
    try: return memo[0]
    except KeyError:
        # Hit the end of the list.
        if i >= len(subjects):
            if bestSubset == None or subsetValue > bestSubsetValue:
                # Found a new best.
                memo[0] = subset[:], subsetValue
                return subset[:], subsetValue
            else:
                # Keep the current best.
                memo[0] = bestSubset, bestSubsetValue
                return bestSubset, bestSubsetValue
        else:
            s = subjects[i]
            # Try including subjects[i] in the current working subset.
            if subsetWork + s[WORK] <= maxWork:
                subset.append(i)
                bestSubset, bestSubsetValue = dpAdvisorHelper(subjects,
                        maxWork, i+1, bestSubset, bestSubsetValue, subset,
                        subsetValue + s[VALUE], subsetWork + s[WORK], memo)
                subset.pop()
            bestSubset, bestSubsetValue = dpAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue, subsetWork, memo)
            memo[0] = bestSubset, bestSubsetValue
            return bestSubset, bestSubsetValue

#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    filename = 'subjects.txt'
    max_work = 15
    # subject_dict = loadSubjects(filename)
    subject_dict = {'6.00': (16, 8), '1.00': (7, 7), '6.01': (5, 3), '15.01': (9, 6)}
    # start_time = time.time()
    
    adv_subjects = dpAdvisor(subject_dict, max_work)
    print numCalls
    # end_time = time.time()
    printSubjects(adv_subjects)
    adv_subjects = bruteForceAdvisor(subject_dict, max_work)
    # print numCalls
    # total_time = end_time - start_time
    printSubjects(adv_subjects)
    # print "Total time with max_work = %d is %0.4f seconds" %(max_work, total_time)

numCalls = 0
dpTime()

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.
