from hstest.stage_test import *
from hstest.test_case import TestCase

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class RPSTest(StageTest):

    def __init__(self, module_to_test: str):
        super().__init__(module_to_test)
        self.wins = 0
        self.draws = 0
        self.loses = 0
        self.file_name = 'rating.txt'

    def generate(self) -> List[TestCase]:
        valid_input_cases = ["Tom\nrock\npaper\nscissors\npaper\nscissors\nrock\npaper\nscissors\n!exit",
                             "Tom\nscissors\nscissors\nscissors\n!exit"]
        invalid_input_cases = ["Tom\nrock\npaper\npaper\nscissors\nblabla\n!exit",
                               "Tom\nrock\ninvalid\n!exit",
                               "Tom\nrock\nrock\nrock\nrock-n-roll\n!exit"]
        tests = list()
        # Cases that check multiple input
        [tests.append(
            TestCase(
                stdin=inp,
                attach=len(inp.split('\n')) - 2,
                check_function=self.check_valid_inputs,
                files={self.file_name: 'Bob 350\nJane 200\nAlex 400'}
            )
        ) for inp in valid_input_cases]
        # Cases that check invalid input
        [tests.append(
            TestCase(
                stdin=inp,
                check_function=self.check_invalid_input,
                files={self.file_name: 'Bob 350\nJane 200\nAlex 400'}
            )
        ) for inp in invalid_input_cases]
        # Case that checks using random module
        long_input = 'Tim\n'
        for _ in range(100):
            long_input += 'rock\n'
        long_input += '!exit'
        tests.append(
            TestCase(
                stdin=long_input,
                attach='rock',
                check_function=self.check_results,
                files={self.file_name: 'Bob 350\nJane 200\nAlex 400'}
            ))
        # Case that checks pints in file
        temp = long_input.split('\n')
        temp[-2] = '!rating'
        long_input = '\n'.join(temp)
        tests.append(
            TestCase(
                stdin=long_input,
                attach='rock',
                check_function=self.check_file,
                files={self.file_name: 'Bob 350\nJane 200\nAlex 400'}
            ))
        return tests

    @staticmethod
    def check_invalid_input(reply: str, attach) -> CheckResult:
        if 'invalid' not in reply.lower():
            return CheckResult.wrong('Looks like your program doesn\'t handle invalid inputs!\n'
                                     'You should print \'Invalid input\' if input can\'t be processed')
        return CheckResult.correct()

    @staticmethod
    def check_valid_inputs(reply: str, attach) -> CheckResult:
        results = 0
        results += reply.lower().count('sorry')
        results += reply.lower().count('draw')
        results += reply.lower().count('well done')
        if results != attach:
            return CheckResult.wrong('Not enough results of the games were printed!\n'
                                     'Tried to input {} actions and got {} results of the games.\n'
                                     'May be you don\'t handle all inputs.\n'
                                     'And make sure you print the result  of the game in the correct format after each valid input!'
                                     .format(attach, results))
        return CheckResult.correct()

    def check_results(self, reply: str, ignored) -> CheckResult:

        self.wins = reply.lower().count('well done')
        self.draws = reply.lower().count('draw')
        self.loses = reply.lower().count('sorry')

        wrong_randomize = CheckResult.wrong("The results of the games: {} wins, {} draws and {} loses\n"
                                            "Looks like you don't use random module to choose random option!\n"
                                            "The number of wins, draws and loses should be approximately the same.\n"
                                            "Make sure you output the results of the games like in examples!\n"
                                            "If you pretty sure that you use random module try to rerun the tests!\n"
                                            .format(self.wins, self.draws, self.loses))
        if self.loses < 20:
            return wrong_randomize
        if self.draws < 20:
            return wrong_randomize
        if self.wins < 20:
            return wrong_randomize

        return CheckResult.correct()

    def check_file(self, reply: str, ignored) -> CheckResult:

        for line in reply.split('\n'):
            lower_line = line.lower()
            if 'well done' in lower_line and 'scissors' not in lower_line:
                return CheckResult.wrong(
                    'Wrong result of the game:\n> rock\n{}\nRock can only bit scissors!'.format(line))
            elif 'draw' in lower_line and 'rock' not in lower_line:
                return CheckResult.wrong(
                    'Wrong result of the game:\n> rock\n{}\nThe game ends with a draw only when user option and computer choose the same option'.format(
                        line))
            elif 'sorry' in lower_line and 'paper' not in lower_line:
                return CheckResult.wrong(
                    'Wrong result of the game:\n> rock\n{}\nOnly paper can bit rock!'.format(line))

        self.wins = reply.lower().count('well done')
        self.draws = reply.lower().count('draw')
        self.loses = reply.lower().count('sorry')

        correct_points = self.wins * 100 + self.draws * 50

        if str(correct_points) not in reply:
            return CheckResult.wrong('Looks like you incorrectly calculated the player\'s score!\n'
                                     'For each draw, add 50 point to the score. For each user\'s win, add 100 to his/her score.\n'
                                     'In case the user loses, don\'t change the score. ')

        return CheckResult.correct()


if __name__ == '__main__':
    RPSTest("rps.game").run_tests()
