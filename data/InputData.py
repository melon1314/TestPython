from model.SpecialInput import SpecialInput


class InputData:
    input_list = []
    model_list = []

    def init_input_list(self,list):
        self.input_list = list

    def clear_input_list(self):
        self.input_list = []

    def init_input_model_list(self):
        input1 = SpecialInput(aliance='Fizz')
        input2 = SpecialInput(aliance='Buzz')
        input3 = SpecialInput(aliance='Whizz')
        self.model_list.append(input1)
        self.model_list.append(input2)
        self.model_list.append(input3)
        return self.model_list

    def clear_model_list(self):
        self.model_list = []

    def update_model_by_input_list(self, input_list):
        for index in range(len(input_list)):
            self.model_list[index].raw_int = int(input_list[index])
        return self.model_list

    def get_model_list(self):
        return self.model_list


input_data = InputData()


