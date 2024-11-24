# Testing 11.1

### Testing Plan
This testing plan focuses on verifying the functionality that prevents users from casting duplicate votes in the CLA department ballot system. Here's a breakdown of the testing elements:

1) Scenario: A user attempts to submit a vote for President and Vice President.
2) Expected Behavior:
The user's vote is successfully recorded.
The user's voted_department field is set to True.
Any subsequent attempt to submit a vote redirects the user to the Records page with a 302 status code (indicating a temporary redirect).
3) Test Cases:
Test 1.1: Successful vote submission (covered by test_prevent_duplicate_votes)
Test 1.2: Attempt to submit a duplicate vote (covered by test_prevent_duplicate_votes)

### Testing Framework

This unit test case utilizes Django's built-in testing framework (django.test). Django's framework provides a robust and convenient way to write unit tests for any django project.

### Justification:
1) **Integration with Django**: Using Django's testing framework ensures seamless integration with the Django application structure and tools.
2) **Ease of Use**: Django's framework offers a familiar syntax and structure for developers already comfortable with Django development.
3) **Adequate Testing**: This framework allows for efficient testing of the specific functionality without the need for a more complex framework.

### Execution and Result
<img src="./assets/testing/testing-1.png" width=600 height=600>  <br>


# Testing 12.1/12.2

### Testing Plan


### Testing Framework


### Justification:


### Execution and Result
