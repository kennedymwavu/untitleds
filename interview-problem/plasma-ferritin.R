# read in the data:
athlete_data <- read.csv(
  file = "Sports Data CW 2021.csv", 
  header = TRUE
)


# ----Task 1----
# Test if plasma ferritin concentration differs between male and female athletes. 
# Make sure that the assumptions of the test are satisfied. 
# State null and alternative hypotheses and your conclusion.

# Test for normality of the data first; Use shapiro-wilk normality test.
# H0: The data are normally distributed
# H1: The data are not normally distributed

# shapiro-wilk normality test for male plasma ferretin concentration:
male_normality <- with(athlete_data, shapiro.test(x = Ferr[Sex == "male"]))
male_normality$p.value

# shapiro-wilk normality test for female plasma ferretin concentration:
female_normality <- with(athlete_data, shapiro.test(x = Ferr[Sex == "female"]))
female_normality$p.value

# The p-values for both males and males are less than the significance level 
# 0.05 implying that the distributions of the data are significantly 
# different from the normal distribution.

# This implies we can't use the unpaired two-samples t-test. We'll instead 
# use the non-parametric unpaired two-samples wilcoxon test:

ferritin_diff <- wilcox.test(
  formula = Ferr ~ Sex, data = athlete_data, exact = FALSE
)

ferritin_diff

ferritin_diff$p.value

# Since the p-value is less than the significance level `alpha = 0.05`, we 
# can conclude that males' median plasma ferritin concentration is 
# significantly different from females' median plasma ferritin concentration
# with a p-value of ferritin_diff$p.value

# ----Task 2----
# Randomly divide the dataset into two sets, training (n1 = 141) and 
# testing (n2 = 61):

# training indices:
set.seed(91)
n1 <- sample(x = nrow(athlete_data), size = 141, replace = FALSE)

# training data:
training <- athlete_data[n1, ]

# testing data:
testing <- athlete_data[-n1, ]

# |- a----
# (a) Write down the equation of a regression model with Ferr as the response 
# and other variables as predictors except for the Sport variable.

# all column names:
colnms <- colnames(training)

# predictor variables:
predictors <- colnms[!colnms %in% c("Sport", "Ferr")]

# Equation:
frmla <- reformulate(predictors, response = "Ferr")
frmla

# |- b----
# fit the model:
full_model <- lm(formula = frmla, data = training)
summary(full_model)

# The only significant predictors are:
# Sex, LBM & BMI

# fit a model with only the significant predictors:
smaller_model <- lm(
  formula = Ferr ~ Sex + LBM + BMI, data = training
)
summary(smaller_model)

# Is a the full model better than the smaller model?

# Compare the two models using anova test:
comparison <- anova(smaller_model, full_model)
comparison

# The p-value = 0.732 is not sufficiently low (less than 0.05) 
# implying that the complex model (full_model) is not significantly better 
# than the simpler model (smaller_model). We should favor the smaller 
# model. In other words, the full model is not better than the 
# smaller model.

# |- c----
# Check the linear regression assumptions for the model fitted in part (b). 
# Do the assumptions hold for your model?

# 1. Linearity of the data
# The linearity assumption can be checked by inspecting the 
# Residuals vs Fitted plot:
plot(full_model, 1)

# There is a pattern in the residual plot meaning we can't assume 
# a linear relationship between the predictors and outcome variable

# 2. Normality of residuals:
# The QQ plot of residuals can be used to visually check the normality 
# assumption. The normal probability plot of residuals should 
# approximately follow a straight line.
plot(full_model, 2)

# all the points do not fall approximately along this reference line, 
# so we can assume non-normality.

# shapiro test for normality:
shapiro.test(full_model$residuals)

# The p-value is less than 0.05, confirming that the residuals 
# are not normally distributed.

