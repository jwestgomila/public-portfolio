This CSV parser was created as part of a University of Bath Artificial Intelligence MSc assignment and I scored 85%. Example parsed output of the './test-indoor_temperature.csv' files can be found below.

```
Failed to convert '1235.78' in line '21' to majority data type '<class 'datetime.datetime'>'
Failed to convert '' in line '11' to majority data type '<class 'float'>'
Failed to convert '' in line '2' to majority data type '<class 'float'>'
Failed to convert 'Empty' in line '18' to majority data type '<class 'float'>'
Failed to convert 'Empty' in line '20' to majority data type '<class 'float'>'
Failed to convert '' in line '6' to majority data type '<class 'int'>'
DateTime                          Humidity  Temperature  Temperature_2  Temperature_range (high)  Temperature_range (low)  Text                           

2016-10-09 00:00:00               54        21.93        5              22.8                      21.0                     Jake
Hello "Molly"             
2016-10-10 00:00:00+00:00         52        21.7         7              23.6                                               John Doe                       
2016-10-11 00:00:00               51        21.36        8              23.0                      19.9                                                    
2016-11-10 00:00:00               51        21.44        9              23.6                      20.0                     Jane, the "Explorer"           
2016-10-12 00:00:00               52        21.22        10             22.3                      20.1                                                    
2016-10-12 00:00:00               55        22.5                        23.5                      21.0                     Some text with, comma          
2016-10-13 00:00:00+00:00         50        21.0         11             22.0                      20.0                     Quoted "Text" Example          
1970-08-22 09:16:54               49        20.75        12             22.1                      19.5                                                    
2016-10-15 00:00:00               53        22.1         13             23.3                      21.0                     A "messy" entry                
2016-10-15 00:00:00               54        21.65        14             22.4                      20.0                     Mixed quotes                   
2016-10-16 00:00:00               52                     15             23.0                      20.2                                                    
2016-10-17 00:00:00               53        21.8         16             23.2                      20.5                     Trailing space                 
2016-10-18 12:34:00               55        22.0         17             23.8                      21.0                     Multiline
text field           
2016-10-19 00:00:00               50        21.1         18             22.5                      20.0                     Text with "quotes" and , commas
2016-10-20 00:00:00               52        21.9         19             23.1                      20.8                                                    
2016-10-20 09:00:00               51        21.5         20             22.0                      20.0                     Timestamp text                 
2016-10-21 14:00:00.123000+02:00  53        21.85        21             23.3                      20.7                     Another "test" case            
2016-10-21 14:00:00.123000+02:00  53        21.85        22                                       20.7                                                    
2016-10-22 00:00:00               53        21.85        23             24.0                      20.7                     Unquoted row                   
2016-10-23 14:00:00.123000+02:00  53        21.85        24                                       20.7                                                    
                                  53        21.85        25             22.5                      20.7                     No quotes on date   
```