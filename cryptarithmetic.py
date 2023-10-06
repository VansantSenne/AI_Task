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
    puzzle = st.text_input("Voer de cryptarithmetic puzzel in (bijv. TO + GO = OUT):").upper()
    
    if st.button("Oplossen"):
        if puzzle:
            solution = solve_puzzle(puzzle)
            if solution:
                st.success("Oplossing gevonden:")
                for var, val in solution.items():
                    st.write(f"{var}: {val}")
            else:
                st.warning("Geen oplossing gevonden.")
        else:
            st.warning("Voer een geldige cryptarithmetic puzzel in.")

if __name__ == "__main__":
    main()
