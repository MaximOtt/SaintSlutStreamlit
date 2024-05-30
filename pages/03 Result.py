import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

if 'a' not in st.session_state:
    st.session_state.a = 0
    st.switch_page('Welcome.py')

st.header("Result")
answers = st.session_state.answers_1 + st.session_state.answers_2
df = pd.DataFrame(answers)

theory_score = df[df['dimension'] == 'theory']['answer'].mean()
reality_score = df[df['dimension'] == 'reality']['answer'].mean()

st.write(f"Theory Score: {theory_score}")
st.write(f"Reality Score: {reality_score}")

# Scatter plot
fig, ax = plt.subplots()

# Scatter plot with large points
dot_color='cyan'
ax.vlines(reality_score, 0, theory_score, linestyle="dashed", color=dot_color, zorder = 0)
ax.hlines(theory_score, 0, reality_score, linestyle="dashed", color=dot_color, zorder = 0)
ax.scatter(reality_score, theory_score, s=100, color=dot_color, zorder = 1)

# Setting limits
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)

# Setting background color
fig.patch.set_facecolor('darkgrey')
fig.patch.set_alpha(0.0)
ax.set_facecolor('darkgrey')

# Customizing the axes
ax.spines['bottom'].set_color('white')
ax.spines['bottom'].set_linewidth(2)
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_color('white')
ax.spines['left'].set_linewidth(2)
ax.spines['left'].set_position('zero')
ax.spines['top'].set_color('white')
ax.spines['top'].set_linewidth(2)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('white')
ax.spines['right'].set_linewidth(2)
ax.spines['left'].set_position('zero')

ax.set_xticks([])
ax.set_yticks([])
ax.xaxis.set_tick_params(labelbottom=False)
ax.yaxis.set_tick_params(labelleft=False)

ax.patch.set_facecolor('red')
ax.patch.set_alpha(0.0)

# Adding arrows
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, color='white')
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, color='white')
ax.plot(0, 0, "<k", transform=ax.get_yaxis_transform(), clip_on=False, color='white')
ax.plot(0, 0, "vk", transform=ax.get_xaxis_transform(), clip_on=False, color='white')

# Labeling the axes limits
ax_limit_font_size = 14
ax.text(2.5, 0.07, 'Slut', fontsize=ax_limit_font_size, color='white', verticalalignment='bottom', horizontalalignment='right')
ax.text(-2.5, 0.07, 'Saint', fontsize=ax_limit_font_size, color='white', verticalalignment='bottom', horizontalalignment='left')
ax.text(0.07, 2.5, 'Slut', fontsize=ax_limit_font_size, color='white', verticalalignment='top', horizontalalignment='left')
ax.text(0.07, -2.5, 'Saint', fontsize=ax_limit_font_size, color='white', verticalalignment='bottom', horizontalalignment='left')

# Remove the plot border (spines)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# ax.spines['left'].set_visible(False)
# ax.spines['bottom'].set_visible(False)

# Adding text on the axes
ax_label_font_size = 11
ax.text(0.5, 0.07, 'What you are', fontsize=ax_label_font_size, color='white', verticalalignment='bottom')
ax.text(-0.2, -0.07, 'What you', fontsize=ax_label_font_size, color='white', rotation=90, verticalalignment='top')
ax.text(-0.2, 0.07, 'wish you were', fontsize=ax_label_font_size, color='white', rotation=90, verticalalignment='bottom')

# Adding value labels to points
# for i, txt in enumerate(zip(theory_score, reality_score)):
#     ax.annotate(f'({txt[0]}, {txt[1]})', (theory_score[i], reality_score[i]), fontsize=12, color='white')


st.pyplot(fig)