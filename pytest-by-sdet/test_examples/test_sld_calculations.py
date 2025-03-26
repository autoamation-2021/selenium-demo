import re

def calculate_factors(data):
        print("data",data)
        # Function to handle numeric extraction and finding the maximum value
        def parse_max_value(value):
            """
            Extracts the maximum numeric value from a range, single number, or comma-separated values.
            """
            numbers = [int(num) for num in re.findall(r'\d+', value.replace(",", ""))]
            return max(numbers) if numbers else 0  # Return highest number found
       
        # Function to extract min and max values from a range
        def parse_min_max(value):
            """
            Extracts the minimum and maximum numeric values from a range, single number, or comma-separated values.
            If the value is "200+", it treats both min and max as 200.
            """
            numbers = [int(num) for num in re.findall(r'\d+', value.replace(",", ""))]
            if "200+" in value:
                return 200, 200  # Special case for "200+"
            return (min(numbers), max(numbers)) if numbers else (0, 0)
 
        # 1 Member Factor Calculation
        business_members_str = data.get(
            "How many business members are there in your community? (estimate the total number of businesses who could be your members)", "0"
        )
        current_members_str = data.get("How many members do you have?", "0")
        min_members, max_members = parse_min_max(current_members_str)
 
        business_members = parse_max_value(business_members_str)
        current_members = parse_max_value(current_members_str)
       
 
        print("business_members:", business_members)
        print("min_members:", min_members)
        print("max_members:", max_members)
 
        # Calculate Member Factor
        member_factor = business_members / current_members if current_members > 0 else 0
        member_factor_value = 18 if member_factor < 20 else 20  
 
 
        # 2
        # Audience Factor Calculation
        audience_size_str = data.get(
            "What is the size of your audience in your community? (estimate the number of potential customers for your members)", "0"
        )
 
        audience_size = parse_max_value(audience_size_str)
 
 
        # 25,000-50,000,  - 0.8
        # 50,001- 100,000, - 0.8
        # 100,001-250,000,  - 0.9
        # 250000+           -0.9
 
        # Determine Audience Factor
        if 25000 <= audience_size <= 100000:
            audience_factor = 0.8
        elif audience_size > 100000:  # 100001+
            audience_factor = 0.9
        else:  # Less than 25000
            audience_factor = 0.0
 
        print("audience_size:", audience_size)
        print("audience_factor:", audience_factor)
 
 
        # 3
        # Comms Factor Calculation
        email_list_str = data.get("E-Mail Distribution List?", "0")
        social_followers_str = data.get("Estimate Social Medial Followers on all channels?", "0")
 
        email_list_size = parse_max_value(email_list_str)
        social_followers_size = parse_max_value(social_followers_str)
       
        # Determine Email Factor
        if email_list_size <= 1000:
            email_factor = 0.7
        elif 1001 <= email_list_size <= 5000:
            email_factor = 0.7  # Fix: 1001-5000 should be 0.7
        elif 5001 <= email_list_size:
            email_factor = 0.9  # 5001+ should be 0.9
 
        # Determine Social Media Factor
        if social_followers_size <= 1000:
            social_factor = 0.7
        elif 1001 <= social_followers_size <= 2500:
            social_factor = 0.7  # Fix: 1001-2500 should be 0.7
        elif 2501 <= social_followers_size:
            social_factor = 0.9  # 2501+ should be 0.9
 
        # Comms Factor Calculation (Taking an Average)
        comms_factor = (email_factor / social_factor)
 
 
 
        #   4
        # Priority Factors
        priority_factors = {
            'low': 1.0,
            'medium': 1.1,
            'high': 1.2,
        }
 
 
 
        # 5️ Member Growth Calculation
        grow_membership_priority = data.get("Grow Membership", "low").lower()  # Default to 'low'
        priority_multiplier = priority_factors.get(grow_membership_priority, 1.0)
 
 
        low_member_growth = (min_members + (member_factor_value * 2)) * 1.4 * priority_multiplier
        high_member_growth = (max_members + (member_factor_value * 4)) * 1.4 * priority_multiplier
 
 
 
        # 6 Member Engagement Calculation (Low & High)
        audience_size_str = data.get(
            "What is the size of your audience in your community? (estimate the number of potential customers for your members)", "0"
        )
        min_audience_members, max_audience_members = parse_min_max(audience_size_str)
        if min_audience_members==max_audience_members:
           audience_midpoint= 250
        else:
        #    Need to check //
           audience_midpoint = (min_audience_members + max_audience_members) // 2
        # Priority factor for member attrition
        member_attrition_priority = data.get("Decrease Member Attrition?", "medium").lower()
        member_attrition_priority_factor = priority_factors.get(member_attrition_priority, 1.1)
 
        # Calculate Low Member Engagement
        low_member_engagement = (
            audience_midpoint * audience_factor * comms_factor * member_attrition_priority_factor
        )
       
        # Calculate High Member Engagement
        high_member_engagement = low_member_engagement * 1.2
 
        print("low_member_engagement:", low_member_engagement)
        print("high_member_engagement:", high_member_engagement)
 
 
        #7 Revenue Growth
        # Priority factor for member attrition
        member_attrition_priority = data.get("Increase Revenues?", "medium").lower()
        priority_increase_revenue = priority_factors.get(member_attrition_priority, 1.1)
        low_revenue_growth = low_member_growth * audience_factor * 600 * priority_increase_revenue
        high_revenue_growth = high_member_growth * audience_factor * 600 * priority_increase_revenue
 
 
        #8 Economic Impact
        # Priority factor for member attrition
        low_economic_impact = low_member_growth * comms_factor * priority_multiplier * 3600
        high_economic_impact = high_member_growth * comms_factor *  priority_multiplier * 4200
 
 
        return {
            'member_growth': (int(low_member_growth), int(high_member_growth)),
            'revenue_growth': (int(low_revenue_growth), int(high_revenue_growth)),
            'member_engagement': (int(low_member_engagement), int(high_member_engagement)),
            'economic_impact': (int(low_economic_impact), int(high_economic_impact)),
        }
 
 
 
 
 
data = {
    'Estimate Social Medial Followers on all channels?': '1,001 -2,500',
    'E-Mail Distribution List?': '1001-5000',
    'How many members do you have?': '200+',
    'What is the size of your audience in your community? (estimate the number of potential customers for your members)': '25,000-50,000',
    'How many business members are there in your community?': '5000+',
    'Grow Membership': 'Low',
    'Increase Revenues': 'Medium',
    'Decrease Member Attrition?': 'Medium'
}
 
value = calculate_factors(data)
print(value)