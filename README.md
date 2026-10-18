#ModelLab
**[Launch model-lab](https://model-lab-qgmhwjy6adtjgp5pnrb3dk.streamlit.app/)**
**A tool tha experiments with machine learning models in your browser!**

model-lab is a tool to get people to understand how machine-learning models work by visualizing their processes and resaults through interactive, schematic representations.


It features 4 classification algorithms: Random Forest, Logistic Regression, K-nearest Neighbours and Decision Trees
You have acces to interactive hyperparameters, evaluation metrics(f1_score, precision_score, recall_score). You can also visualize them by using a confusion matrix and download model predictions for future analysis.

model-lab uses the built-in sklearn dataset wine. it has 178 samples, 13 columns, and 3 wine classes

#How to run it localy:

##Step 1:
Clone the repository:
```bash
git clone https://github.com/onooyt-prog/model-lab.git
cd model-lab
```
##Step 2:
Create and activate a virtual envioroment:

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
**(Windows)**

```bash
python -m venv .venv
source .venv/bin/activate
```
**(Linux)**

##Step 3:

Install dependecies and start the application
```bash
pip install pandas matplotlib streamlit scikit-learn
streamlit run app.py
```
<!--
# Title	Main heading
## Subtitle	Smaller heading
### Section	Even smaller heading
**text**	Bold text
*text*	Italic text
`code`	Inline code
- item	Bullet list
1. item	Numbered list
[text](URL)	Clickable link
![alt](URL)	Embed an image
---	Horizontal line
> text	Blockquote
~~text~~	Strikethrough
```python	Start a Python code block (close with three backticks)
-->