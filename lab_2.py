"""6.009 Lab 4 -- Boolean satisfiability solving"""

import sys
sys.setrecursionlimit(10000)
# NO ADDITIONAL IMPORTS
import json
import time

def satisfying_assignment(formula):
    """
    Find a satisfying assignment for a given CNF formula.
    Returns that assignment if one exists, or None otherwise.

    >>> satisfying_assignment([])
    {}
    >>> x = satisfying_assignment([[('a', True), ('b', False), ('c', True)]])
    >>> x.get('a', None) is True or x.get('b', None) is False or x.get('c', None) is True
    True
    >>> satisfying_assignment([[('a', True)], [('a', False)]])
    """
    assignment = {}
#    for clause in formula:
#        for literal in clause: d 
#            if literal[0] not in assignment:
#                assignment[literal[0]] = None
#            else:
#                continue 
    if formula == []:
#        print('empty')
        return assignment
    
    # determine if there is any unit-length clause in formula
    def unit_clause(formula):
        for clause in formula:
            if len(clause) == 1:
                return (clause[0])
        return None
    
    # determine if there are clauses in formula that conflict with each other; if yes, no mapping exists, return None
#    def conflict_formula(formula, current):
#        record = {}
#        for clause in formula:
##            print(clause)
#            if len(clause) == 1 and current in clause[0]:
##                print('yes')
#                if current not in record:
#                    record[current] = clause[0][1]
#                elif clause[0][1] != record[current]:
##                    print('wow')
#                    return True
#                else:
#                    continue
#        return False
    
    # determine if there are literals in clause that conlict with each other; if yes, return True
    def conflict_clause(clause, current):
        record = {}
        for literal in clause:
            if current in literal:
                if current not in record:
                    record[current] = literal[1]
                elif literal[1] != record[current]:
                    return True
                else:
                    continue
        return False
    
    # determine if the clause is satisfied
#    def determine_clause(clause, current):
#       for literal in clause:
#           if current[0] in literal and current[1] == literal[1]:
##                print('yes')
#               return True
#       return False
    
    # determine if the literal is satisfied
    def determine_literal(literal, current, value):
        if current != None:
            if literal[1] == value:
                return True
            else:
                return False
        else:
            return 'need_to_assign'
        
    # determine if the clause is satisfied   
    def determine_clause(clause, assignment):
        result = 0
        for literal in clause:
            if literal[0] in assignment:
                current = literal[0]
                value = assignment[current]
            else:
                current = None
                value = None
                
            if determine_literal(literal, current, value) == True:
                return True
            elif determine_literal(literal, current, value) == 'need_to_assign':
                result += 1
            else:
                continue
        if result == 0:
            return False
        else:
            return 'continue'
    
    # determine if the formula is satisfied
    def determine_formula(formula, assignment):
        need = 0
        for clause in formula:
            if determine_clause(clause, assignment) == False:
#                print('pass')
                return False
            elif determine_clause(clause, assignment) == 'continue':
#                print('fail')
                need += 1
                continue
            else:
                continue
        if need == 0:
            return True
        else:
            return 'next_recursion'
    
    # formula processing
    def formula_process(formula, current, value):
        formula_new = []
        for clause in formula:
#            print(clause)
#            clause_new = clause[:]
#            clause_new = []
#            if conflict_clause(clause, current):
##                print('conflict clause')
##                    assignment[current] = None
#                for literal in clause:
#                    if current in literal:
#                        clause_new.remove(literal)
#                formula_new.append(clause_new)
#                        
#            else:
#                for literal in clause:
##                    print('current new formula is: ')
##                    print(formula_new)
#                    if current in literal:
#                        if value != literal[1]:
##                            print('remove current literal')
#                            clause_new.remove(literal)
##                            print(clause_new)
#                        else:
##                            print('current clause is correct')
#                            clause_new = []
#                            break
#                    else:
#                        continue
#                if clause_new == []:
#                    continue
#                else:
#                    formula_new.append(clause_new)
#        return formula_new
        
#            clause_new = clause[:]
            clause_new = []
#            if conflict_clause(clause, current):
##                print('conflict clause')
##                    assignment[current] = None
#                for literal in clause:
#                    if current in literal:
#                        clause_new.remove(literal)
#                formula_new.append(clause_new)
                        
#            else:
            for literal in clause:
#                    print('current new formula is: ')
#                    print(formula_new)
                if current in literal:
                    if value != literal[1]:
#                            print('remove current literal')
#                        clause_new.remove(literal)
                        continue
#                            print(clause_new)
                    else:
#                            print('current clause is correct')
#                        clause_new = []
                        clause_new = ['True']
                        break
#                        break
                else:
#                    continue
                    clause_new.append(literal)
                    
            if clause_new == ['True']:
                continue
            elif clause_new == []:
                return None
            else:
                formula_new.append(clause_new)
                
        return formula_new
    
    # recursion function
    def recur_assign(formula, assignment):
        
#        print(formula)
#        print('current formula is: ')
#        print(formula)
#        print('assignmeng is: ')
#        print(assignment)
        # try to find unit-length clause
        unit = unit_clause(formula)
#        print(unit)
        
        # if yes, set current to variable in unit-length clause
        if unit != None:
            current = unit[0]
            value = unit[1]
            new_assignment = assignment.copy()
            new_assignment[current] = value
#            print(current)
#            if determine_formula(formula, assignment) == True:
#                return assignment
#            elif determine_formula(formula, assignment) == False:
#                return None
#            else:
#                formula_new = formula_process(formula, current, value)
#                return recur_assign(formula_new, assignment)
            formula_new = formula_process(formula, current, value)
            if formula_new == []:
                return new_assignment
            elif formula_new == None:
                return None
            else:
#                if recur_assign(formula_new, assignment) == None:
#                    return None
#                else:
                return recur_assign(formula_new, new_assignment)
        # if no, set current to variable in first literal of first clause of the formula
        else:
            current = formula[0][0][0]
            new_assignment = assignment.copy()
            for value in [True, False]:
                new_assignment[current] = value
#                if determine_formula(formula, new_assignment) == True:
#                    return new_assignment
#                elif determine_formula(formula, new_assignment) == False:
#                    continue
#                else:
#                    formula_new = formula_process(formula, current, value)
#                    return recur_assign(formula_new, new_assignment)
                formula_new = formula_process(formula, current, value)
                if formula_new == []:
                    return new_assignment
                elif formula_new == None:
                    continue
                else:
#                   if recur_assign(formula_new, new_assignment) == None:
#                       continue
#                   else:
                    return recur_assign(formula_new, new_assignment)
            return None
#            return None
#        if all(formula):
#            print('yes')
#            assignment[current] = value
#            return assignment
        
        # determine if the current formula is satisfied; if yes, store the bool_value of current variable into dictionary
#        if determine_formula(formula, (current, value)):
#            print('all_true')
#            assignment[current] = value
#            print(assignment)
#            return assignment
#        
#        # if there are conflicting cluases in formula, return None
#        if conflict_formula(formula, current):
#            print('conflict')
#            return None
##            print(assignment)
        
#        print(assignment)
#        return assignment
#    print(recur_assign(formula, assignment))
    return recur_assign(formula, assignment)       
            

def boolify_scheduling_problem(student_preferences, session_capacities):
    """
    Convert a quiz-room-scheduling problem into a Boolean formula.

    student_preferences: a dictionary mapping a student name (string) to a set
                         of session names (strings) that work for that student
    session_capacities: a dictionary mapping each session name to a positive
                        integer for how many students can fit in that session

    Returns: a CNF formula encoding the scheduling problem, as per the
             lab write-up
    We assume no student or session names contain underscores.
    """
    
    student_list = list(student_preferences.keys())
    room_list = list(session_capacities.keys())
    
    # 1. student in his/her preferred room
    def student_pref(student_preferences, result = None):
        if result == None:
            result = []
        for student in student_preferences:
            clause = []
            for room in student_preferences[student]:
                clause.append([student + '_' + room, True])
            result.append(clause)
        return result
    
    # generate combo based on list of students
    def combination(n, student_list, length, combo = None, result = None):
#        print(n)
#        print(result)
        if result == None:
            result = []
        
        if combo == None:
            combo = []
            
        if n == 0 and len(combo) == length:
#            print('before append')
#            print(combo)
#            print('end')
            result.append(combo)
            return result
        
        for i in range(len(student_list)):
            current = student_list[i]
#            print('current student: ' + current)
#            if len(combo) < n:
            if current not in combo and set(combo + [current]) not in result:
#                print('combo')
#                print(combo)
                result = combination(n-1, student_list[1:], length, combo + [current], result)
            else:
                continue
#        print(result)
        return result
    
    # 2. Each student in exactly one session
    def exactly_one(student_list, room_list):
        l1 = []
        room_combo = combination(2, room_list, 2)
        
        for student in student_list:
            for combo in room_combo:
                l2 = []
                for room in combo:
                    l2.append([student + '_' + room, False])
                l1.append(l2)
        return l1
    
    # 3. No oversubscribed room
    def session_cap(session_capacities, student_list, result = None):
        if result == None:
            result = []
        for room in session_capacities:
            capability = session_capacities[room]
            if capability >= len(student_list):
                continue
            else:
                num = capability + 1
                combo_student = combination(num, student_list, num)
                for combo in combo_student:
                    l = []
                    for student in combo:
                        l.append([student + '_' + room, False])
                    result.append(l)
        return result
    
    rule1 = student_pref(student_preferences)
    rule2 = exactly_one(student_list, room_list)
    rule3 = session_cap(session_capacities, student_list)
    return rule1 + rule2 + rule3

if __name__ == '__main__':
#    import doctest
#    _doctest_flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
#    doctest.testmod(optionflags=_doctest_flags)
#    result = satisfying_assignment([[('a', True)], [('a', False)]])
    
    true = True
    false = False
    formula = [[["c", true]], [["a", true]], [["a", false], ["b", false]], [["a", true], ["c", false]], [["c", true]]]
#    with open('1000_5_10000.json') as f:
#        soduku  = json.loads(f.read())
#    start = time.time()
#    result_s = satisfying_assignment(soduku)
#    end = time.time()
#    print(end - start)
#    result = satisfying_assignment(formula)
#    student_dict = {'Alice': {'basement', 'penthouse'},
#                            'Bob': {'kitchen'},
#                            'Charles': {'basement', 'kitchen'},
#                            'Dana': {'kitchen', 'penthouse', 'basement'}}
#    print(student_pref(student_dict))
    
    start = time.time()
    with open('15_5.json') as f:
        data  = json.loads(f.read())
    student_preferences = data[0]
    session_capacities =  data[1]
    formula = boolify_scheduling_problem(student_preferences, session_capacities)
    result = satisfying_assignment(formula)
    end = time.time()
    print(end - start)
    def combination(n, student_list, length, combo = None, result = None):
#        print(n)
#        print(result)
        if result == None:
            result = []
        
        if combo == None:
            combo = []
            
        if n == 0 and len(combo) == length:
#            print('before append')
#            print(combo)
#            print('end')
            result.append(combo)
            return result
        
        for i in range(len(student_list)):
            current = student_list[i]
#            print('current student: ' + current)
#            if len(combo) < n:
            if current not in combo and sorted(combo + [current]) not in result:
#                print('combo')
#                print(combo)
                result = combination(n-1, student_list[1:], length, combo + [current], result)
            else:
                continue
        
        return result
#    student_list = ['Alice','Bob','Charles','Dana']
#    result = combination(2, student_list, 2)
#    assignment = {'a': True, 'b': False, 'c': False}
#    clause = [['a', False],['b', True], ['c', True]]
#    result = determine_clause(clause,assignment)