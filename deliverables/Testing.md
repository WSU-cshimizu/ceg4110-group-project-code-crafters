# Testing 11.1

### Testing Plan
The testing plan focuses on unit testing to verify that the CLA department ballot system correctly prevents duplicate votes. The test will check that when a user attempts to submit multiple votes for the same department (after already casting a vote), the system will redirect them to the Records page instead of allowing a second vote. The primary focus is ensuring that the logic preventing duplicate votes is functioning as expected at the unit level.

### Testing Framework

This unit test case utilizes Django's built-in testing framework (django.test). Django's framework provides a robust and convenient way to write unit tests for any django project.

### Justification:
1) Choice of Plan:

    This testing plan fits well within the team's software development plan by focusing on the core functionality of preventing duplicate votes. Unit testing allows us to isolate this specific feature and verify its correctness independently, ensuring a solid foundation before integrating it with other parts of the system.

2) Choice of Framework:

    * Achievability: Django's built-in testing framework is readily available and well-integrated with the Django application structure, making it easily achievable for our team.

    * Adequacy: This framework provides the necessary tools to effectively test the desired functionality. By using Django's testing client, we can simulate user interactions, including submitting votes, and assert the expected outcomes, such as redirects or error messages.

### Test case: Preventing duplicate users from voting
<img src="./assets/testing/testing-1.png" width=800 height=600>  <br>


# Testing 12.1/12.2

### Testing Plan
The plan involves functional testing to verify the responsiveness of the voting interface across different browsers and devices. The primary focus will be on testing key UI elements like the main container, navigation bar, and footer, ensuring that they are properly displayed on desktop, tablet, and mobile devices.

### Testing Framework
We will use Selenium WebDriver for automated testing. Selenium is ideal for this task as it supports cross-browser testing, allowing us to run tests on Chrome, Firefox, and Edge. It also facilitates simulating different screen sizes to validate the responsive layout of the interface.

### Justification:
This testing approach is appropriate because it aligns with the need to ensure cross-browser compatibility and responsive design across a range of devices. Selenium was chosen for its robustness and wide support for different browsers, making it feasible to automate the testing process across multiple platforms. The scope of the testing is well-defined, focusing on the visibility and layout of critical UI components, which are key aspects of functional testing. This method ensures that the application performs as expected in various environments, covering the essential functionality of the system.

### Test case: Responsiveness in different browers(Chrome/Edge/FireFox) for different devices(Windows/Tablet/Mobile)
<img src="./assets/testing/responsiveness.png" width=800 height=500>  <br>