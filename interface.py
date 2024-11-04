import gradio as gr

def create_abstract_noun(verb):
    if verb.endswith("ати") or verb.endswith("яти") or verb.endswith("іти"):
        abs_noun = verb[:-2] + "нн" + "я"
        result = f"Абстрактний іменник: {abs_noun}, суфікс абстрактності -нн"
    elif verb.endswith("ити"):
        abs_noun = verb[:-3] + "енн" + "я"
        result = f"Абстрактний іменник: {abs_noun}, суфікс абстрактності -енн"
    else:
        result = "Не вдалося згенерувати абстрактний іменник для введеного дієслова."
    
    return result

def process_input(user_inp):
    user_inp = user_inp.strip().lower()
    
    if user_inp.endswith("ся") or user_inp.endswith("сь"):
        non_reflexive_verb = user_inp[:-2]
        return create_abstract_noun(non_reflexive_verb)
    else:
        return create_abstract_noun(user_inp)

with gr.Blocks(css="""
                * {
                  margin-bottom: 20px;
               }
               .my-button {
                  background-color: #4CAF50;
                  color: white;
                  width: 600px;
                  margin: 0 auto;
                  height: 50px
               }
                .title {
                  text-align: center; 
                  font-size: 30px
               }
""") as demo:
    gr.Markdown("<h1 style='text-align: center; font-size: 30px;'>Синтез абстрактних іменників</h1>")
    with gr.Column():
        inp = gr.Textbox(placeholder="малювати", label="Інфінітив")
        btn = gr.Button("Утворити абстрактний іменник", elem_classes="my-button")
    with gr.Column():
        out = gr.Textbox(label="Результат")

    btn.click(fn=process_input, inputs=inp, outputs=out)

demo.launch()
