---
type: idea
status:
  - archived
tags: []
created: 2025-11-10
AI_prompt: true
---

**Role:** You are an AI data analyst and Python programmer.

**Goal:** Your task is to write a Python script that takes a single CSV file (exported from a "Project Plan" Excel file) and generates a PNG heatmap visualizing the weekly "ongoing" workload for each team member.

**Input:** A single CSV file named `Project Plan.xlsx - Tasks.csv`.

**Output:** A single PNG image file named `staff_weekly_workload_heatmap_ongoing.png`.

---

### Key Requirements for the Chart

1. **Chart Type:** Heatmap (using Seaborn).
    
2. **Y-Axis:** `Staff Member` names.
    
3. **X-Axis:** Weeks, formatted as `MMM-YY, Wx` (e.g., `Nov-25, W3`). The weeks **must** be in chronological order.
    
4. **Cell Values:** The count of "ongoing" tasks for that staff member in that week.
    
5. **"Ongoing" Definition:** A task is "ongoing" in a given week if its `Effective Start Date` is on or before that week, AND its `Effective Due Date` is on or after that week.
    
6. **Filtering:** All tasks/rows with an "Unassigned" staff member must be excluded from the chart.
    
7. **Annotations:** The chart must show the numerical task count in each cell (`annot=True`).
    
8. **Color Scale:** Use a "Reds" color map (`cmap="Reds"`).
    
9. **Grid:** Include thin lines between cells to form a clear grid (`linewidths=.5`).
    

---

### Detailed Processing Steps

Here is the exact logic you must follow to process the data and create the chart:

**1. Load Libraries:**
- You will need `pandas` for data manipulation, `seaborn` for plotting, and `matplotlib.pyplot` for saving the figure.
    

**2. Load Data:**
- Read the input file `Project Plan (1).xlsx - Tasks.csv` into a pandas DataFrame.
    

**3. Clean Assignee Names:**
- Fill any `NaN` values in the `Assigned To` column with a placeholder string (e.g., `TEMP_UNASSIGNED`).
    
- Split the `Assigned To` column by the semicolon (`;`) character to handle multiple assignees.
    
- Explode the DataFrame so that each assignee for a task gets their own row.
    
- Create a new `Staff Member` column by cleaning the `Assigned To` values. The cleaning logic is: if the name starts with `Creagy-`, remove that prefix.
    
- Filter out (i.e., remove) all rows where the `Staff Member` is `TEMP_UNASSIGNED` or `Unassigned`.
    

**4. Define Effective Dates for "Ongoing" Logic:**
- Convert the `Start date`, `Due date`, and `Created Date` columns to datetime objects.
- Create an `Effective_Start` column: Use the `Start date`, but if it's missing (NaT), fall back to the `Created Date`.
- Create an `Effective_Due` column: Use the `Due date`.
- **Crucially:** Filter the DataFrame to keep _only_ the rows that have **both** a valid `Effective_Start` AND a valid `Effective_Due`. Tasks without both dates cannot be used for this logic.
    

**5. Generate Weekly Timeline:**
- Find the minimum `Effective_Start` and maximum `Effective_Due` from your filtered tasks.
- Generate a `pd.date_range` with a weekly frequency (`freq='W'`) that spans this entire project timeline. This gives you a list of all weeks (we'll call it `Week Starting`).
    

**6. Calculate Ongoing Tasks (The Core Logic):**

- Create a "cross join" between your filtered tasks DataFrame and the weekly timeline DataFrame. The result should be a new, large DataFrame with a row for _every task_ duplicated for _every week_.
- Filter this new DataFrame using the "ongoing" logic:
    - `keep` rows where `(Effective_Start <= Week Starting)` AND `(Effective_Due >= Week Starting)`
        
- Group this filtered data by `Staff Member` and `Week Starting`, and get the `size()` to find the count of ongoing tasks. Reset the index and rename the count to `Task Count`.
    

**7. Format for Heatmap:**
- **Create Week Labels:** Create a new `Week Label` column from the `Week Starting` column.
    
    - The format is `MMM-YY, Wx` (e.g., `Nov-25, W3`).
        
    - `MMM-YY` is from `week_ts.strftime('%b-%y')`.
        
    - `Wx` is the week of the month, calculated as `f"W{(week_ts.day - 1) // 7 + 1}"`.
        
- **Pivot the Data:** Pivot the aggregated DataFrame to create a matrix suitable for a heatmap:
    
    - `index='Staff Member'`
        
    - `columns='Week Label'`
        
    - `values='Task Count'`
        
- **Sort Columns Chronologically:** The pivot will sort columns alphabetically. You must fix this. Create an ordered list of `Week Label` strings based on the original `Week Starting` dates. Then, use `.reindex(columns=ordered_labels)` on your pivoted DataFrame to sort the columns chronologically.
    
- **Fill NaNs:** Fill any `NaN` values in the final pivoted matrix with `0`.
    

**8. Plot with Seaborn:**

- Set a large figure size (e.g., `figsize=(22, 10)`) to accommodate all the weeks.
    
- Use `sns.heatmap` to plot the final matrix.
    
- Pass the following parameters: `annot=True`, `fmt=".0f"`, `cmap="Reds"`, `linewidths=.5`.
    
- Set the title, x-label, and y-label.
    
- Use `plt.tight_layout()` to ensure labels are not cut off.
    
- Save the figure as `staff_weekly_workload_heatmap_ongoing.png`.