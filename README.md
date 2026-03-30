# Technical Assessment

---

Welcome to Your Technical Assessment. To reflect a real-world development environment, you have access to an AI Coding Assistant integrated directly into this IDE. We encourage you to use it to accelerate your workflow, but remember: we are evaluating your engineering decisions, not the AI’s.

### Using the AI Assistant

You can use the assistant for:

*   **Boilerplate & Syntax**: Generating repetitive code or looking up library signatures.
*   **Refactoring**: Improving the readability or efficiency of your initial implementation.
*   **Debugging**: Identifying logical errors or edge cases in your code.

### Guidelines for Success

**Ownership**: You are responsible for every line of code submitted. If the AI suggests a bug or an insecure pattern and you commit it, it reflects on your assessment.

**Verification**: Always read and understand AI-generated code before incorporating it. You may be asked to explain the logic behind specific blocks during the follow-up interview.

**Optimization**: AI often provides the 'most likely' solution, not necessarily the most performant. Ensure the output meets the specific constraints of the problem.

> Pro-Tip
> Treat the AI as a junior pair programmer. It’s great at following directions, but it needs you to provide the architectural vision and the final 'sanity check.'

### Evaluation Criteria

We aren't looking for 'perfect' AI prompts. We are looking for:

*   **Problem Decomposition**: How you break the task into parts.
*   **Critical Thinking**: Your ability to spot and correct AI hallucinations.
*   **Code Quality**: Proper naming, modularity, and handling of edge cases.

Good luck! We’re excited to see what you build. See below for additional instructions related to your specific assignment(s).

---

## Challenge 1: Payroll Calculator

Build a payroll calculator that computes monthly salary for employees based on their type and applicable deductions.

The system must support three employee types:

*   `FULL_TIME` (fixed monthly salary)
*   `PART_TIME` (hourly rate × hours worked, **max 120 hours/month**)
*   `CONTRACTOR` (daily rate × days worked)

Apply these tax brackets to gross salary:

| Bracket      | Salary Range   | Tax Rate |
|--------------|----------------|----------|
| 1            | $0 - $1000     | 0%       |
| 2            | $1001 - $3000  | 10%      |
| 3            | $3001 - $5000  | 20%      |
| 4            | Over $5000     | 30%      |

Deductions include:

*   health insurance (**$150 flat, only for `FULL_TIME`**)
*   retirement contribution (**5% of gross, optional flag per employee**)
*   union dues (**$50 flat if employee is union member**)

Implement the following classes:

*   `Employee` (`id`, `name`, `employeeType`, `payRate`, `isUnionMember`, `hasRetirement`)
*   `PaySlip` (`employee`, `grossPay`, `taxAmount`, `deductions map`, `netPay`)
*   `PayrollProcessor`

The `PayrollProcessor` must provide the following methods:

*   `calculateGrossPay(employee, hoursOrDays)`
*   `calculateTax(grossPay)`
*   `calculateDeductions(employee, grossPay)`
*   `generatePaySlip(employee, hoursOrDays)`
*   `processMonthlyPayroll(employeeList)`

**Round all currency values to 2 decimal places.**

Demonstrate with at least 6 employees covering all types and deduction combinations.

---

## Challenge 2: Text Document Analyzer

Create a text document analyzer that reads a plain text file and generates comprehensive word statistics.

The analyzer must:

1.  Read the input file and normalize text by converting to lowercase and removing punctuation (**keep only alphanumeric characters and spaces**).
2.  Tokenize the text into individual words, ignoring words with fewer than **3 characters**.
3.  Count the frequency of each unique word and store in a map/dictionary.
4.  Exclude common stop words (provide a list of **at least 20**: the, and, is, at, which, on, a, an, as, are, was, were, been, be, have, has, had, do, does, did).
5.  Calculate the following statistics:
    *   total word count
    *   unique word count
    *   average word length
    *   longest word
    *   most frequent word

Implement the following classes:

*   `TextReader` (reads and normalizes file content)
*   `WordCounter` (tokenizes and counts frequencies)
*   `StatisticsReport` (generates formatted output)

Provide the following methods:

*   `getTopNWords(n)` returning the `n` most frequent words **sorted by count descending**
*   `getWordsStartingWith(prefix)` returning matching words **sorted alphabetically**
*   `exportReport(outputFilePath)` writing all statistics to a formatted text file

Include a sample text file of **at least 500 words** for testing.