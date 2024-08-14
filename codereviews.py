# PART 3. CODE REVIEWS. PLEASE DO A CODE REVIEW FOR THE FOLLOWING SNIPPET. ADD YOUR REVIE SUGGESTIONS INLINE AS PYTHON COMMENTS



# ------------------------------------------------------------------------------- # # ------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------- # # ------------------------------------------------------------------------------- #



# Problem 1. Find values from the data associated with keys

# def get_value(data, key, default, lookup=None, mapper=None):

# """
# Finds the value from data associated with key, or default if the
# key isn't present.
# If a lookup enum is provided, this value is then transformed to its
# enum value.
# If a mapper function is provided, this value is then transformed
# by applying mapper to it.
# """

# # It raise KeyError if key is missing
# # Suggestion: if key is missing, try .get() ensure not getting KeyError
# # try:
# #     return_value = data[key]
# # except KeyError:
# #     return_value = default


# Original code
# return_value = data[key]  

# # It checks if return_value is empty or None
# # Suggestion: Try to handle false values
# #  if not return_value:
#     #return_value = default

# #Original Code
# if return_value is None or return_value == "":
#     return_value = default

# # Lookup deforms the value, try .get(), ensure not getting KeyError

# #Original Code
# if lookup:
#     return_value = lookup[return_value]  # Suggestion: return_value = lookup.get(return_value, default)



# # apply the mapper to the value, if we have it
# # Suggestion: if we have the mapper, try the callable
# # if mapper and callable(mapper):
#     #return_value = mapper(return_value)


# #Original Code
# if mapper:                                            

#     return_value = mapper(return_value)
# return return_value



# ------------------------------------------------------------------------------- # # ------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------- # # ------------------------------------------------------------------------------- #

# Problem 2. Add an ending of ftp


# def ftp_file_prefix(namespace):
#     """
#     Given a namespace string with dot-separated tokens, returns the
#     string with the final token replaced by 'ftp'.
#     Example: a.b.c => a.b.ftp
#     """
#     ## Splits the namespace by dots and removes the last token, then '.ftp' is joined by + to the tokens
#     ## Suggestion: Split the string, remove the last part by using .remove() and based on the length of the string, join the parts and plus the '.ftp' to the not removed string
#     parts = namespace.split(".")
#     if len(parts) > 1:
#         last_part = parts[-1]
#         parts.remove(last_part)
#     else:
#         raise ValueError("We need 2 parts to complete.")
#     return ".".join(parts) + '.ftp'

# print(ftp_file_prefix("a.b.c")) 
# print(ftp_file_prefix("x.y.z"))
# print(ftp_file_prefix("single"))
    
#     #Original Code
#     #return ".".join(namespace.split(".")[:-1]) + '.ftp'




# ------------------------------------------------------------------------------- # # ------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------- # # ------------------------------------------------------------------------------- #




# Problem 3. String to Boolean

# def string_to_bool(string):
#     """
#     Returns True if the given string is 'true' case-insensitive,
#     False if it is 'false' case-insensitive.
#     Raises ValueError for any other input.
#     """
#     # Change the letters of the string to lower and check if it is 'true'
#     # Second row returns True if the string matches 'true'

#     # Suggestion: Use the .strip().lower() to convert lower and handle extra spaces

#     #new_string = string.strip().lower()


#     #Original Code
#     if string.lower() == 'true':
#         return True
    
#     # Change the letters of the string to lower and check if it is 'false'
#     # Second row returns False if the string matches 'false'

#     #Suggestion: Apply simplicity and get a new condition if it is a 'true', beside the 'false'
#     # if new_string == 'true':
#         #return True
#     # if new_string == 'false':
#         #return False

#     #Original Code
#     if string.lower() == 'false':
#         return False  
    
    
#     # It request to raise a ValueError if string is neither true nor false
#     # Raise the ValueError if new_string is either 'true' or 'false' 
#     # raise ValueError('Please make sure inpit is either "true" or "false" ')


#     #Original Code
#     raise ValueError(f'String {string} is neither true nor false')






# ------------------------------------------------------------------------------- # # ------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------- # # ------------------------------------------------------------------------------- #



# Problem 4. Config from the Dict

# def config_from_dict(dict):
#     """
#     Given a dict representing a row from a namespaces csv file,
#     returns a DAG configuration as a pair whose first element is the
#     DAG name and whose second element is a dict describing the DAG's properties.
#     """

#     # request for the value of 'Namespace' from the dict we have
#     # Suggestion: Use dict.get() to handle erorrs and defaults.
#     # namespace = dict.get('Namespace', 'default_namespace')

#     #Original Code
#     namespace = dict['Namespace']




#     # Returns a tuple named DAG as a dictionary
#     # Suggestion: For a simplicity and error handling, we can use again dict.get() to handle errors and defaults. 
#     # dag_name = dict.get('Airflow DAG', 'default_dag_name')  # Replace 'default_dag_name' with a sensible default

#     #Original Code
#     return (
#         dict['Airflow DAG'],  # First component 
#         {
#             # it sets the available delta days to 0
#             # If this value will change, we should make it a variable.
#             # min_delta_days = config.get('delta_days', 0)
            
#             #Original code
#             "earliest_available_delta_days": 0,

#             # Change 'lif' encoding to 'json'
#             # Suggestion: Use a configiuration file, call config to have it as configuration source. 
#             # encoding = config.get('lif_encoding', 'json') 

#             #Original Code
#             "lif_encoding": 'json',

#             # it uses get_value to find the 'Available Start Time', '07:00' is a default
#             # Use dict.get() for a simplified code, and try to handle the default values.
#             # starttime = dict.get('Available Start Time', '07:00')

#             #Original Code
#             "earliest_available_time":
#             get_value(dict, 'Available Start Time', '07:00'),

#             # it uses get_value to find the 'Available End Time', '08:00' is a default
#             # Suggestion: use dict.get() to have simplified code.
#             # endtime = dict.get('Available End Time', '08:00')

#             #Original COde
#             "latest_available_time":
#             get_value(dict, 'Available End Time', '08:00'),



#             # use the get_value to find the 'Requires Schema Match', then converts to boolean, default as 'True'
#             # Suggestion: Bring all of them in the same row under get_value to make more readable and callable the values.
#             # new_schema_match = get_value(dict, 'Requires Schema Match', 'True', mapper=string_to_bool)


#             #Original Code
#             "require_schema_match":
#             get_value(dict, 'Requires Schema Match', 'True',
#                       mapper=string_to_bool),

#             # get_value is used to find the schedule_interval, it is default  '1 7 * * *'
#             # Suggestion: Check if the default value is default for all cases.
#             # suggested_schedule = dict.get('Schedule', '1 7 * * *')



#             #Original Code
#             "schedule_interval":
#             get_value(dict, 'Schedule', '1 7 * * * '),

#             # Get_values is used to find the 'Delta Days' value, default as 'DAY_BEFORE', there is the lookup, if value of it is provided
#             # Should get a feedback of values for Delta Days lookups for all valid values. 
#             # delta_days = get_value(dict, 'Delta Days', 'DAY_BEFORE', lookup=DeltaDays)



#             #Original Code
#             "delta_days":
#             get_value(dict, 'Delta Days', 'DAY_BEFORE',
#                       lookup=DeltaDays),

#             # get_value is used to find the 'File Naming Pattern', default answer is 'None'
#             # Suggestion: Make sure, None is used as default to not get errors.
#             # ftp_wildcard = dict.get('File Naming Pattern', None)


#             #original Code
#             "ftp_file_wildcard":
#             get_value(dict, 'File Naming Pattern', None),

#             # Get_value is used to find the 'FTP File Prefix', ftp_file_prefix function is called
#             # Suggestion: This part of code must handle empty and None too
#             # ftp_prefix = get_value(dict, 'FTP File Prefix', ftp_file_prefix(namespace))


#             #Original Code
#             "ftp_file_prefix":
#             get_value(dict, 'FTP File Prefix',
#                       ftp_file_prefix(namespace)),


#             # Store the 'Namespace' in the configuration  
#             # Suggestion: 
#             # if not namespace:
#             #     raise ValueError("No Namespace")

#             #Original Code
#             "namespace": namespace
#         }
#     )

