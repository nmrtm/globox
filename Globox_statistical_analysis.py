import numpy as np
import pandas as pd
import math
from statsmodels.stats.proportion import proportions_ztest
from scipy import stats
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/Users/namratamuralidharan/Downloads/Globox_python_analysis_data - Sheet1.csv')
alpha = 0.05


# CONVERSION RATE ANALYSIS
#sample size
nA = df[df['group'] == 'A'].shape[0]
nB = df[df['group'] == 'B'].shape[0]

#no of conversions
converted_A = df[(df['group'] == 'A') & (df['conversion'] == 'converted')].shape[0]
converted_B = df[(df['group'] == 'B') & (df['conversion'] == 'converted')].shape[0]

#conversion rate
pA = converted_A / nA
pB = converted_B / nB


# Z-Test (pooled proportions)
z_stat, p_val_conv = proportions_ztest([converted_B, converted_A], [nB, nA])
print("\n---- Conversion Rate Hypothesis Test ----")
print(f"Z-statistic = {z_stat:.4f}, P-value = {p_val_conv:.5f}")
if p_val_conv < alpha:
    print ("✅ Statistically significant. Null hypothesis is rejected.")
else:
    print ("❌ Not statistically significant. Null hypothesis cannot be rejected.")


# Cohen’s h (effect size)
cohen_h = 2 * abs(math.asin(math.sqrt(pB)) - math.asin(math.sqrt(pA)))
print(f"Cohen’s h = {cohen_h:.4f} → ", end='')

if cohen_h >= 0.8:
    print("Interpretation: Large practical difference in conversion rates (h ≥ 0.8).")
elif cohen_h >= 0.5:
    print("Interpretation: Medium practical difference in conversion rates (h ≥ 0.5).")
elif cohen_h >= 0.2:
    print("Interpretation: Small but meaningful practical difference in conversion rates (h ≥ 0.2).")
else:
    print("Interpretation: Effect size is below the threshold for practical significance (h < 0.2).")


# Confidence Interval (unpooled)
se_diff = math.sqrt((pA * (1 - pA)) / nA + (pB * (1 - pB)) / nB)

z_crit = 1.96 #(for 95% condifence interval)

moe = z_crit * se_diff

ci_lower = (pB - pA) - moe
ci_upper = (pB - pA) + moe

print(f"95% CI for (pB - pA): [{ci_lower:.4f}, {ci_upper:.4f}]")


# Error Bars Viz
seA = math.sqrt(pA * (1 - pA) / nA)
seB = math.sqrt(pB * (1 - pB) / nB)

groups = ['Group A (Control)', 'Group B (Treatment)']
conversion_rates_pct = [pA * 100, pB * 100]
errors_pct = [z_crit * seA * 100, z_crit * seB * 100]
colors = ['#c2bebd', '#8b4b68']

plt.figure(figsize=(7, 5))
bars = plt.bar(groups, conversion_rates_pct, yerr=errors_pct, capsize=10, color=colors)

for i, bar in enumerate(bars):
    height = bar.get_height()
    err = errors_pct[i]
    plt.text(bar.get_x() + bar.get_width() / 2, height + err + 0.3,
             f"{conversion_rates_pct[i]:.2f}% ± {err:.2f}%",
             ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.ylabel('Conversion Rate (%)')
plt.title('Conversion Rates with 95% Confidence Intervals')
plt.ylim(0, max(conversion_rates_pct) + max(errors_pct) + 2)
plt.tight_layout()
plt.show()



# AVERAGE SPEND ANALYSIS
#group by spending
spend_A = df[df['group'] == 'A']['spend']
spend_B = df[df['group'] == 'B']['spend']


#Welch's t-test (unequal variances)
t_stat, p_val_spend = stats.ttest_ind(spend_A, spend_B, equal_var=False)

print("\n---- Average Spend Hypothesis Test ----")
print(f"T-statistic = {t_stat:.4f}, P-value = {p_val_spend:.5f}")
if p_val_spend < alpha:
    print ("✅ Statistically significant. Null hypothesis is rejected.")
else:
    print ("❌ Not statistically significant. Null hypothesis cannot be rejected.")


# Cohen's d
mean_A = np.mean(spend_A)
mean_B = np.mean(spend_B)

std_A = np.std(spend_A, ddof=1)
std_B = np.std(spend_B, ddof=1)

pooled_std = np.sqrt((std_A**2 + std_B**2) / 2)

cohen_d = abs((mean_B - mean_A) / pooled_std)

print(f"Cohen’s d = {cohen_d:.4f} → ", end='')

if cohen_d >= 0.8:
    print("Interpretation: Large practical difference in conversion rates (h ≥ 0.8).")
elif cohen_d >= 0.5:
    print("Interpretation: Medium practical difference in conversion rates (h ≥ 0.5).")
elif cohen_d >= 0.2:
    print("Interpretation: Small but meaningful practical difference in conversion rates (h ≥ 0.2).")
else:
    print("Interpretation: Effect size is below the threshold for practical significance (h < 0.2).")


# Confidence Interval (unpooled)
nA = len(spend_A)
nB = len(spend_B)

mean_diff = mean_B - mean_A

se_diff = np.sqrt((std_A**2 / nA) + (std_B**2 / nB))
df_denom = ((std_A**2 / nA)**2 / (nA - 1)) + ((std_B**2 / nB)**2 / (nB - 1))
df_eff = ((std_A**2 / nA) + (std_B**2 / nB))**2 / df_denom
t_crit = stats.t.ppf(1 - alpha/2, df_eff)
moe = t_crit * se_diff

ci_lower = mean_diff - moe
ci_upper = mean_diff + moe

print(f"95% CI for (μB - μA): [{ci_lower:.2f}, {ci_upper:.2f}]")


# Error Bars Viz
means = [mean_A, mean_B]
errors = [t_crit * std_A / np.sqrt(nA), t_crit * std_B / np.sqrt(nB)]

plt.figure(figsize=(7, 5))
bars = plt.bar(groups, means, yerr=errors, capsize=10, color=colors)

for i, bar in enumerate(bars):
    height = bar.get_height()
    err = errors[i]
    plt.text(bar.get_x() + bar.get_width() / 2, height + err + 0.2,
             f"{means[i]:.2f} ± {err:.2f}",
             ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.title("Average Spend per User by Group (95% Confidence Intervals)")
plt.ylabel("Average Spend")
plt.tight_layout()
plt.show()
