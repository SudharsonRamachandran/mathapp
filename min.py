import pandas as pd
import numpy as np
import streamlit as st
import base64

# Web App Title
st.markdown('''
# **The Math App**
---
''')

# Upload CSV data
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["xlsx"])

# Show the DataFrame if all columns except the first column are numeric
if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_excel(uploaded_file)
        return csv
    df = load_csv()
    
    # Check if all columns except the first column are numeric
    if df.iloc[:, 1:].apply(lambda x: pd.to_numeric(x, errors='coerce').notnull().all()).all():
        st.header('**Input DataFrame**')
        st.write(df)
 
        # Add a button to calculate the minimum values
        if st.button('Calculate Minimum Values'):
            # Calculate the minimum value for each column by the first column
            # Get the list of column names except for the first column
            columns = [col for col in df.columns if col != df.columns[0]]
            # Group the DataFrame by the first column and calculate the minimum value for each column
            results = []
            for col in columns:
                id_groups = df.groupby(df.columns[0])
                min_values = id_groups.min()[col]
                # Combine the results into a single DataFrame
                results_df = pd.DataFrame(min_values)
                results_df.columns = [f"{col}_min"]
                # Add the results for this column to the overall results list
                results.append(results_df)

            # Combine the results for all columns into one DataFrame
            combined_results = pd.concat(results, axis=1)
            st.header('**Minimum Value by the first column**')
            st.write(combined_results)
            
            # Download button for minimum values
            tsv = combined_results.to_csv(index=True, sep='\t')
            b64 = base64.b64encode(tsv.encode()).decode()
            href = f'<a href="data:file/tsv;base64,{b64}" download="minimum_values.tsv">Download TSV file</a>'
            st.markdown(href, unsafe_allow_html=True) 
            
        # Add a button to calculate the maximum values
        if st.button('Calculate Maximum Values'):
            # Calculate the maximum value for each column by the first column
            # Get the list of column names except for the first column
            columns = [col for col in df.columns if col != df.columns[0]]
            # Group the DataFrame by the first column and calculate the maximum value for each column
            results = []
            for col in columns:
                id_groups = df.groupby(df.columns[0])
                max_values = id_groups.max()[col]
                # Combine the results into a single DataFrame
                results_df = pd.DataFrame(max_values)
                results_df.columns = [f"{col}_max"]
                # Add the results for this column to the overall results list
                results.append(results_df)

            # Combine the results for all columns into one DataFrame
            combined_results = pd.concat(results, axis=1)
            st.header('**Maximum Value by the first column**')
            st.write(combined_results)

            # Download button for maximum values
            tsv = combined_results.reset_index().to_csv(index=True, sep='\t')
            b64 = base64.b64encode(tsv.encode()).decode()
            href = f'<a href="data:file/tsv;base64,{b64}" download="maximum_values.tsv">Download TSV file</a>'
            st.markdown(href, unsafe_allow_html=True) 
            
        # Add a button to calculate the mean values
        if st.button('Calculate Mean Values'):
            # Calculate the mean value for each column by the first column
            # Get the list of column names except for the first column
            columns = [col for col in df.columns if col != df.columns[0]]
            # Group the DataFrame by the first column and calculate the mean value for each column
            results = []
            for col in columns:
                id_groups = df.groupby(df.columns[0])
                mean_values = id_groups.mean()[col]
                # Combine the results into a single DataFrame
                results_df = pd.DataFrame(mean_values)
                results_df.columns = [f"{col}_mean"]
                # Add the results for this column to the overall results list
                results.append(results_df)

            # Combine the results for all columns into one DataFrame
            combined_results = pd.concat(results, axis=1)
            st.header('**Mean Value by the first column**')
            st.write(combined_results)

            # Download button for mean values
            tsv = combined_results.reset_index().to_csv(index=True, sep='\t')
            b64 = base64.b64encode(tsv.encode()).decode()
            href = f'<a href="data:file/tsv;base64,{b64}" download="mean_values.tsv">Download TSV file</a>'
            st.markdown(href, unsafe_allow_html=True)
            
        # Add a button to calculate the median values
        if st.button('Calculate Median Values'):
            # Calculate the median value for each column by the first column
            # Get the list of column names except for the first column
            columns = [col for col in df.columns if col != df.columns[0]]
            # Group the DataFrame by the first column and calculate the median value for each column
            results = []
            for col in columns:
                id_groups = df.groupby(df.columns[0])
                median_values = id_groups.median()[col]
                # Combine the results into a single DataFrame
                results_df = pd.DataFrame(median_values)
                results_df.columns = [f"{col}_median"]
                # Add the results for this column to the overall results list
                results.append(results_df)

            # Combine the results for all columns into one DataFrame
            combined_results = pd.concat(results, axis=1)
            st.header('**Median Value by the first column**')
            st.write(combined_results)

            # Download button for median values
            tsv = combined_results.reset_index().to_csv(index=True, sep='\t')
            b64 = base64.b64encode(tsv.encode()).decode()
            href = f'<a href="data:file/tsv;base64,{b64}" download="median_values.tsv">Download TSV file</a>'
            st.markdown(href, unsafe_allow_html=True)
            
        # Add a button to calculate the mode values
        if st.button('Calculate Mode Values'):
            # Calculate the mode value for each column by the first column
            # Get the list of column names except for the first column
            columns = [col for col in df.columns if col != df.columns[0]]
            # Group the DataFrame by the first column and calculate the mode value for each column
            results = []
            for col in columns:
                id_groups = df.groupby(df.columns[0])
                mode_values = id_groups[col].apply(lambda x: x.mode()[0])
                # Combine the results into a single DataFrame
                results_df = pd.DataFrame(mode_values)
                results_df.columns = [f"{col}_mode"]
                # Add the results for this column to the overall results list
                results.append(results_df)

            # Combine the results for all columns into one DataFrame
            combined_results = pd.concat(results, axis=1)
            st.header('**Mode Value by the first column**')
            st.write(combined_results)

            # Download button for mode values
            tsv = combined_results.reset_index().to_csv(index=True, sep='\t')
            b64 = base64.b64encode(tsv.encode()).decode()
            href = f'<a href="data:file/tsv;base64,{b64}" download="mode_values.tsv">Download TSV file</a>'
            st.markdown(href, unsafe_allow_html=True)
            
        # Add a button to calculate the percentile 50 values
        if st.button('Calculate Percentile 50 Values'):
            # Calculate the percentile 50 value for each column by the first column
            # Get the list of column names except for the first column
            columns = [col for col in df.columns if col != df.columns[0]]
            # Group the DataFrame by the first column and calculate the percentile 50 value for each column
            results = []
            for col in columns:
                id_groups = df.groupby(df.columns[0])
                percentile_50_values = id_groups.quantile(0.5)[col]
                # Combine the results into a single DataFrame
                results_df = pd.DataFrame(percentile_50_values)
                results_df.columns = [f"{col}_percentile_50"]
                # Add the results for this column to the overall results list
                results.append(results_df)

            # Combine the results for all columns into one DataFrame
            combined_results = pd.concat(results, axis=1)
            st.header('**Percentile 50 Value by the first column**')
            st.write(combined_results)

            # Download button for percentile 50 values
            tsv = combined_results.reset_index().to_csv(index=True, sep='\t')
            b64 = base64.b64encode(tsv.encode()).decode()
            href = f'<a href="data:file/tsv;base64,{b64}" download="percentile_50_values.tsv">Download TSV file</a>'
            st.markdown(href, unsafe_allow_html=True)
        
        # Add a button to calculate the 75th percentile values
        if st.button('Calculate 75th Percentile Values'):
            # Calculate the 75th percentile value for each column by the first column
            # Get the list of column names except for the first column
            columns = [col for col in df.columns if col != df.columns[0]]
            # Group the DataFrame by the first column and calculate the 75th percentile value for each column
            results = []
            for col in columns:
                id_groups = df.groupby(df.columns[0])
                percentile75_values = id_groups.quantile(0.75)[col]
                # Combine the results into a single DataFrame
                results_df = pd.DataFrame(percentile75_values)
                results_df.columns = [f"{col}_75th_percentile"]
                # Add the results for this column to the overall results list
                results.append(results_df)

            # Combine the results for all columns into one DataFrame
            combined_results = pd.concat(results, axis=1)
            st.header('**75th Percentile Value by the first column**')
            st.write(combined_results)

            # Download button for 75th percentile values
            tsv = combined_results.reset_index().to_csv(index=True, sep='\t')
            b64 = base64.b64encode(tsv.encode()).decode()
            href = f'<a href="data:file/tsv;base64,{b64}" download="75th_percentile_values.tsv">Download TSV file</a>'
            st.markdown(href, unsafe_allow_html=True)

else: 
    st.info('Awaiting for CSV file to be uploaded.')
