# Overview of Multivariate Methods

When multivariate analysis is applicable?

Nature of measurement error and its impact

Techniques, guidelines, interpretation

Steps to multivariate model building

multivariate analysis -> influences -> data collection

## Key Terms

1. Type I and II errors

2. **Bivariate partial correlation**: correlation between two sets ...

3. **Bootstrapping**: validating a multivariate model by drawing a large number 
   of sub-samples and estimating models for each sub-sample

4. Dependence technique: regression analysis

5. Dependente variable, Independent variable, Dummy variable

6. Indicator, Interdependence technique

8. Measurement error, Specification error

9. Multicolliniarity: Extent to which a variable can be explained by the other variables in the analysis

10. **Power**: Probability of correctly rejecting the null hypothesis when it is false; that is, correctly finding a hypothesized relationship when it exists
    
11. Practical significance, Reliability, Validity, Variate

12. Metric data (quantitative data), Nonmetric data (qualitative data)

13. Univariate analysis of variance (ANOVA)

## What is Multivariate Analysis

- [X] Effective knowledge creation and management


> "We are drowning in information and starved for knowledge", Tom Peters

## Multivariate Analysis in Statistical Terms

- [X] Create knowledge and thereby improve their decision making

>### Multivariate analysis
> refers to all statistical techniques that simultaneously analyze multiple measurements on individuals or objects under investigation

## Some Basic Concepts of Multivariate Analysis

>### Roots
> univariate and bivariate statistics

### The Variate

> - building block of multivariate analysis
> - a linear combination of variables with empirically determined weights

Variate value $= w_1X_1 + w_2X_2 + \ldots + w_nX_n$ where $X_n$ is
the observed variable and $w_n$ is the weight determined by the
multivariate technique.

## Measurement Scales

> Data can be classified into one of two categories -- nonmetric, qualitative and metric, quantitative -- based on the type of attributes or characteristics they represent.

### Nonmetric Measurement Scales

Nonmetric data describe differences in ty or kind by indicating the presence or absence of a characteristic or property.

>### Nominal Scales
> assigns numbrs as a way to label or identify subjects or objects

>### Ordinal Scales
> "higher" level of measurement precision, variables can be ordered or ranked in relation to the amount of the attribute possessed

### Metric Scales

> metric data are used when subjects differ in amount or degree on a particular attribute

>### Interval Scales
> mathematical operations to be performed

>### Ratio Scales
> absolute zero points

### The Impact of Choice of Measurement Scale

>### 1
> identify the correct measurement scale of each variable used

>### 2
> critical in determining which multivariate techniques are the most applicable to the data

## Measurement Error and Multivariate Measurement

>### Measurement Error
> is the degree to which the observed values are not representative of the "true" values.

> data entry errors, imprecision of the measurements

> All variables used in multivariate techniques must be assumed to have some degree of measurement error

### Validity and Reliablity

>### Validity
> degree to which a measure accurately represents what it is supposed to

>### Reliability
> degree to which the observed variable measures the "true" value and is "error free", opposite of measurement error

### Employing Multivariate Measurement

>### Summated Scales
> several variables are joined in a composite measure to represent a concept (several variables as a **indicators**)

### The Impact of Measurement Error

> cannot be directly seen because they are embedded in the observed variables

> always workto increase reliability and validity

> Poor results are not always due to measurement error, but the presence of measurement error is guaranteed to distort the observed relationships and make the multivariate techniques less powerful.

## Statistical Significance Versus Statistical Power

> All the multivariate techniques, except for cluster analysis and perceptual mapping, are based on the statistical inference of a population's values or relationships among variables from a randomly drawn sample of that population.

### Types of Statistical Error and Statistical Power

> Interpreting statistical inferences requires to specify the acceptable levels of statistical error that result from using a sample (sample error)

>### Type I error, alpha $(\alpha)$
> Type I error is the probability of rejecting the null hypothesis when it is actually true, **false positive**

> specifying an $\alpha$ level $=>$ sets the acceptable limits for error and indicates the probability of conducting that significance exists when actually it really does not

>### Type II error, beta $(\beta)$
> $(\beta)$ associated error with $(\alpha)$, the Type II error is the probability of not rejecting the null hypothesis when it is actually false

> An extension of Type II error is $1 - \beta$, referred to as the **power** of the statistical inference test

> **Power** is the probability of correctly rejecting the null hypothesis when it should be rejected

