import unittest
from src.main.lab import get_complex_output_parser, invoke_complex_chain, get_complex_prompt, invoke_basic_chain
from src.utilities.llm_testing_util import llm_connection_check, llm_wakeup, classify_relevancy

class TestLLMResponses(unittest.TestCase):

    """
    This function is a sanity check for the Language Learning Model (LLM) connection.
    It attempts to generate a response from the LLM. If a 'Bad Gateway' error is encountered,
    it initiates the LLM wake-up process. This function is critical for ensuring the LLM is
    operational before running tests and should not be modified without understanding the
    implications.
    Raises:
        Exception: If any error other than 'Bad Gateway' is encountered, it is raised to the caller.
    """
    def test_llm_sanity_check(self):
        try:
            response = llm_connection_check()
            self.assertIsInstance(response, LLMResult)
        except Exception as e:
            if 'Bad Gateway' in str(e):
                llm_wakeup()
                self.fail("LLM is not awake. Please try again in 3-5 minutes.")
    
    def test_simple_prompt1(self):
        try:
            response = invoke_basic_chain("pizza")
        except:
            self.fail("invoke_basic_chain() raised an exception unexpectedly!")
        self.assertIn("is_food", response)
        self.assertTrue(response["is_food"])
    
    def test_simple_prompt2(self):
        try:
            response = invoke_basic_chain("chicken")
        except:
            self.fail("invoke_basic_chain() raised an exception unexpectedly!")
        self.assertIn("is_food", response)
        self.assertTrue(response["is_food"])
    
    def test_simple_prompt3(self):
        try:
            response = invoke_basic_chain("car")
        except:
            self.fail("invoke_basic_chain() raised an exception unexpectedly!")
        self.assertIn("is_food", response)
        self.assertFalse(response["is_food"])
                
    def test_get_complex_prompt(self):
        prompt_template = get_complex_prompt().messages[-1].prompt.template
        self.assertIn("title", prompt_template)
        self.assertIn("is_family_friendly", prompt_template)
        self.assertIn("genre", prompt_template)
        self.assertIn("run_time", prompt_template)
        self.assertIn("year_released", prompt_template)
    
    def test_get_complex_output_parser(self):
        response_schemas = [item.name for item in get_complex_output_parser().response_schemas]
        self.assertIn("title", response_schemas)
        self.assertIn("is_family_friendly", response_schemas)
        self.assertIn("genre", response_schemas)
        self.assertIn("run_time", response_schemas)
        self.assertIn("year_released", response_schemas)
    
    def test_invoke_complex_chain(self):
        try:
            movie = invoke_complex_chain("The Matrix")
        except:
            self.fail("invoke_complex_chain() raised an exception unexpectedly!")
        self.assertIn("title", movie)
        self.assertIn("is_family_friendly", movie)
        self.assertIn("genre", movie)
        self.assertIn("run_time", movie)
        self.assertIn("year_released", movie)

        self.assertIn("The Matrix", movie["title"])
        self.assertIn("Action", movie["genre"])
        self.assertIn("1999", movie["year_released"])
        self.assertIn("136 minutes", movie["run_time"])
        self.assertEqual(False, movie["is_family_friendly"])    

if __name__ == '__main__':
    unittest.main()