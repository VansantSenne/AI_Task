import streamlit as st
from simpleai.search import CspProblem, backtrack

# Functie om de cryptarithmetic puzzel op te lossen
def solve_puzzle(puzzle):
    lijst = puzzle.split(" ")
    variables = []
    lijst.pop(1)
    lijst.pop(2)
    for i in lijst:
        for j in i:
            variables += j
    variables = set(variables)
    domains = {}
    for k in lijst:
        for i, l in enumerate(k):
            if i == 0:
                domains[l] = list(range(1, 10))
            else:
                domains[l] = list(range(0, 10))

    def constraint_unique(variables, values):
        return len(values) == len(set(values))

    def constraint_add(variables, values):
        fac1 = ""
        fac2 = ""
        result = ""
        for i in lijst[0]:
            fac1 += str(values[variables.index(i)])
        for j in lijst[1]:
            fac2 += str(values[variables.index(j)])
        for k in lijst[2]:
            result += str(values[variables.index(k)])
        fac1 = int(fac1)
        fac2 = int(fac2)
        result = int(result)
        return (fac1 + fac2) == result

    constraints = [
        (variables, constraint_unique),
        (variables, constraint_add),
    ]

    problem = CspProblem(variables, domains, constraints)

    output = backtrack(problem)
    return output

# Streamlit-applicatie
def main():
    st.title("Cryptarithmetic Puzzle Solver")
    puzzle = st.text_input("Enter the cryptarithmetic puzzle (e.g., TO + GO = OUT):").upper()
    
    if st.button("Solve"):
        if puzzle:
            solution = solve_puzzle(puzzle)
            if solution:
                st.success("Solution found:")
                
                # Display the solution with words horizontally beneath each other
                st.write("Digits Solution:")
                digits_line = ""
                for word in puzzle.split():
                    for char in word:
                        if char.isalpha():
                            digits_line += str(solution[char])
                        else:
                            digits_line += char
                    st.write(digits_line)
                    digits_line = ""
                
                st.write("Letters Solution:")
                letters_line = ""
                for word in puzzle.split():
                    for char in word:
                        if char.isalpha():
                            letters_line += char
                        else:
                            letters_line += char
                    st.write(letters_line)
                    letters_line = ""
            else:
                st.warning("No solution found.")
        else:
            st.warning("Enter a valid cryptarithmetic puzzle.")

if __name__ == "__main__":
    main()
