import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Hyperlocal Economy Intelligence",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    app_dir = Path(__file__).resolve().parent
    candidates = [
        app_dir / "hyperlocal_economy_processed.csv",
        app_dir / "data" / "hyperlocal_economy_processed.csv",
    ]
    for csv_path in candidates:
        if csv_path.exists():
            return pd.read_csv(csv_path)
    raise FileNotFoundError(
        "Could not find hyperlocal_economy_processed.csv in expected locations."
    )

df = load_data()

# Header
st.markdown('<div class="main-header">🏙️ Hyperlocal Economy Intelligence System</div>', 
            unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/business.png", width=100)
    st.title("🎯 Navigation")
    
    page = st.radio("Select View:", 
                    ["🏠 Overview", "📊 Data Explorer", "🎯 Investment Finder", 
                     "📈 Analytics", "💼 Business Recommender"])
    
    st.markdown("---")
    st.subheader("🔍 Filters")
    
    # Filters
    cities = st.multiselect("Select Cities:", 
                           options=df['city'].unique(),
                           default=df['city'].unique()[:3])
    
    area_types = st.multiselect("Area Type:",
                                options=df['area_type'].unique(),
                                default=df['area_type'].unique())
    
    score_range = st.slider("Health Score Range:",
                           min_value=0, max_value=100,
                           value=(0, 100))
    
    # Apply filters
    if cities:
        df_filtered = df[df['city'].isin(cities)]
    else:
        df_filtered = df
    
    if area_types:
        df_filtered = df_filtered[df_filtered['area_type'].isin(area_types)]
    
    df_filtered = df_filtered[
        (df_filtered['economic_health_score'] >= score_range[0]) &
        (df_filtered['economic_health_score'] <= score_range[1])
    ]
    
    st.markdown("---")
    st.info(f"📍 Showing {len(df_filtered)} locations")


# PAGE 1: OVERVIEW

if page == "🏠 Overview":
    
    # KPI Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Locations", len(df_filtered),
                 delta=f"{len(df_filtered)/len(df)*100:.1f}% of total")
    
    with col2:
        avg_score = df_filtered['economic_health_score'].mean()
        st.metric("Avg Health Score", f"{avg_score:.1f}",
                 delta=f"{avg_score - df['economic_health_score'].mean():.1f}")
    
    with col3:
        high_potential = len(df_filtered[df_filtered['investment_category']=='High Potential'])
        st.metric("High Potential Areas", high_potential,
                 delta=f"{high_potential/len(df_filtered)*100:.1f}%")
    
    with col4:
        top_city = df_filtered.groupby('city')['economic_health_score'].mean().idxmax()
        st.metric("Top City", top_city)
    
    st.markdown("---")
    
    # Two columns layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Score Distribution")
        fig = px.histogram(df_filtered, x='economic_health_score', 
                          nbins=30, color='investment_category',
                          color_discrete_map={
                              'High Potential': 'green',
                              'Moderate Potential': 'orange',
                              'Low Potential': 'red'
                          })
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🎯 Investment Categories")
        category_counts = df_filtered['investment_category'].value_counts()
        fig = px.pie(values=category_counts.values, names=category_counts.index,
                    color=category_counts.index,
                    color_discrete_map={
                        'High Potential': 'green',
                        'Moderate Potential': 'orange',
                        'Low Potential': 'red'
                    })
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # Top 10 Areas
    st.markdown("---")
    st.subheader("🏆 Top 10 Investment Areas")
    
    top_10 = df_filtered.nlargest(10, 'economic_health_score')
    
    fig = go.Figure(go.Bar(
        x=top_10['economic_health_score'].values,
        y=top_10['area_name'].values,
        orientation='h',
        marker=dict(
            color=top_10['economic_health_score'].values,
            colorscale='RdYlGn',
            showscale=True
        ),
        text=top_10['economic_health_score'].round(1),
        textposition='outside'
    ))
    fig.update_layout(height=500, yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True)


# PAGE 2: DATA EXPLORER

elif page == "📊 Data Explorer":
    
    st.subheader("📊 Interactive Data Explorer")
    
    # Search
    search = st.text_input("🔍 Search by area name:", "")
    if search:
        df_filtered = df_filtered[df_filtered['area_name'].str.contains(search, case=False)]
    
    # Display options
    col1, col2 = st.columns([3, 1])
    with col1:
        sort_by = st.selectbox("Sort by:", 
                              ['economic_health_score', 'monthly_rent', 
                               'property_price_sqft', 'footfall_score'])
    with col2:
        sort_order = st.radio("Order:", ['Descending', 'Ascending'])
    
    # Sort dataframe
    df_display = df_filtered.sort_values(
        sort_by, 
        ascending=(sort_order=='Ascending')
    )
    
    # Select columns to display
    display_cols = st.multiselect(
        "Select columns to display:",
        options=['area_name', 'city', 'area_type', 'locality_type',
                'economic_health_score', 'investment_category', 'monthly_rent',
                'property_price_sqft', 'footfall_score', 'infrastructure_score',
                'recommended_business', 'risk_score'],
        default=['area_name', 'city', 'economic_health_score', 
                'investment_category', 'monthly_rent']
    )
    
    # Display dataframe
    st.dataframe(df_display[display_cols], use_container_width=True, height=400)
    
    # Download button
    csv = df_display[display_cols].to_csv(index=False)
    st.download_button(
        label="📥 Download as CSV",
        data=csv,
        file_name='filtered_data.csv',
        mime='text/csv'
    )
    
    # Statistics
    st.markdown("---")
    st.subheader("📈 Statistics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Numeric Summary:**")
        st.dataframe(df_display[display_cols].describe().round(2))
    
    with col2:
        st.write("**Categorical Summary:**")
        if 'area_type' in display_cols:
            st.write(df_display['area_type'].value_counts())
        if 'investment_category' in display_cols:
            st.write(df_display['investment_category'].value_counts())
    
    with col3:
        st.write("**Missing Values:**")
        missing = df_display[display_cols].isnull().sum()
        if missing.sum() > 0:
            st.write(missing[missing > 0])
        else:
            st.success("No missing values!")


# PAGE 3: INVESTMENT FINDER

elif page == "🎯 Investment Finder":
    
    st.subheader("🎯 Smart Investment Finder")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### Investment Criteria")
        
        budget = st.number_input("Monthly Rent Budget (₹):", 
                                min_value=0, max_value=100000, 
                                value=25000, step=5000)
        
        min_score = st.slider("Minimum Health Score:", 
                             min_value=0, max_value=100, value=60)
        
        preferred_growth = st.multiselect("Preferred Growth:",
                                         ['Growing', 'Stable', 'Declining'],
                                         default=['Growing', 'Stable'])
        
        min_footfall = st.slider("Minimum Footfall Score:",
                                min_value=0, max_value=100, value=50)
    
    with col2:
        st.write("### Location Preferences")
        
        preferred_cities = st.multiselect("Preferred Cities:",
                                         df['city'].unique(),
                                         default=df['city'].unique()[:2])
        
        preferred_locality = st.multiselect("Locality Type:",
                                           ['Commercial', 'Mixed', 'Residential'],
                                           default=['Commercial', 'Mixed'])
        
        max_risk = st.slider("Maximum Risk Score:",
                            min_value=0, max_value=100, value=50)
    
    # Find button
    if st.button("🔍 Find Investment Opportunities", type="primary"):
        
        # Apply criteria
        results = df[
            (df['monthly_rent'] <= budget) &
            (df['economic_health_score'] >= min_score) &
            (df['business_growth'].isin(preferred_growth)) &
            (df['footfall_score'] >= min_footfall) &
            (df['city'].isin(preferred_cities)) &
            (df['locality_type'].isin(preferred_locality)) &
            (df['risk_score'] <= max_risk)
        ].sort_values('economic_health_score', ascending=False)
        
        st.markdown("---")
        
        if len(results) > 0:
            st.success(f"✅ Found {len(results)} matching opportunities!")
            
            # Display top results
            for idx, row in results.head(5).iterrows():
                with st.expander(f"🏆 {row['area_name']}, {row['city']} - Score: {row['economic_health_score']:.1f}"):
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric("Health Score", f"{row['economic_health_score']:.1f}")
                        st.metric("Monthly Rent", f"₹{row['monthly_rent']:,.0f}")
                    
                    with col2:
                        st.metric("Footfall Score", f"{row['footfall_score']:.1f}")
                        st.metric("Risk Score", f"{row['risk_score']:.1f}")
                    
                    with col3:
                        st.metric("Property Price", f"₹{row['property_price_sqft']:,.0f}/sqft")
                        st.write(f"**Growth:** {row['business_growth']}")
                    
                    st.write(f"**Recommended Business:** {row['recommended_business']}")
                    st.write(f"**Area Type:** {row['area_type']} - {row['locality_type']}")
        else:
            st.error("❌ No areas match your criteria. Try relaxing some filters.")


# PAGE 4: ANALYTICS

elif page == "📈 Analytics":
    
    st.subheader("📈 Advanced Analytics")
    
    tab1, tab2, tab3 = st.tabs(["📊 Correlations", "🗺️ Geographic", "💹 Risk-Return"])
    
    # TAB 1: Correlations
    with tab1:
        st.write("### Correlation Analysis")
        
        numeric_cols = ['economic_health_score', 'business_density_score', 
                       'footfall_score', 'infrastructure_score', 'property_value_score',
                       'monthly_rent', 'pedestrian_count_15min']
        
        corr_matrix = df_filtered[numeric_cols].corr()
        
        fig = px.imshow(corr_matrix, 
                       text_auto='.2f',
                       color_continuous_scale='RdBu_r',
                       aspect='auto')
        fig.update_layout(height=600)
        st.plotly_chart(fig, use_container_width=True)
        
        # Scatter plots
        col1, col2 = st.columns(2)
        
        with col1:
            x_var = st.selectbox("X-axis:", numeric_cols, index=5)
        with col2:
            y_var = st.selectbox("Y-axis:", numeric_cols, index=0)
        
        fig = px.scatter(df_filtered, x=x_var, y=y_var, 
                        color='area_type', size='economic_health_score',
                        hover_data=['area_name', 'city'],
                        trendline="ols")
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)
    
    # TAB 2: Geographic
    with tab2:
        st.write("### Geographic Analysis")
        
        # City comparison
        city_stats = df_filtered.groupby('city').agg({
            'economic_health_score': 'mean',
            'monthly_rent': 'mean',
            'property_price_sqft': 'mean',
            'area_id': 'count'
        }).round(2)
        city_stats.columns = ['Avg Score', 'Avg Rent', 'Avg Price/sqft', 'Count']
        city_stats = city_stats.sort_values('Avg Score', ascending=False)
        
        fig = px.bar(city_stats.reset_index(), x='city', y='Avg Score',
                    color='Avg Score', color_continuous_scale='RdYlGn')
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        st.dataframe(city_stats, use_container_width=True)
    
    # TAB 3: Risk-Return
    with tab3:
        st.write("### Risk-Return Analysis")
        
        fig = px.scatter(df_filtered, x='risk_score', y='expected_return',
                        color='investment_category', size='economic_health_score',
                        hover_data=['area_name', 'city'],
                        color_discrete_map={
                            'High Potential': 'green',
                            'Moderate Potential': 'orange',
                            'Low Potential': 'red'
                        })
        
        # Add quadrant lines
        fig.add_hline(y=df_filtered['expected_return'].median(), 
                     line_dash="dash", line_color="gray")
        fig.add_vline(x=df_filtered['risk_score'].median(), 
                     line_dash="dash", line_color="gray")
        
        fig.update_layout(height=600)
        st.plotly_chart(fig, use_container_width=True)
        
        # Best opportunities
        best = df_filtered[
            (df_filtered['risk_score'] < df_filtered['risk_score'].median()) &
            (df_filtered['expected_return'] > df_filtered['expected_return'].median())
        ].nlargest(10, 'expected_return')
        
        st.write("#### 🌟 Best Opportunities (Low Risk + High Return)")
        st.dataframe(best[['area_name', 'city', 'economic_health_score', 
                          'risk_score', 'expected_return']], 
                    use_container_width=True)


# PAGE 5: BUSINESS RECOMMENDER

elif page == "💼 Business Recommender":
    
    st.subheader("💼 AI Business Recommender")
    
    st.write("### Tell us about your business idea:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        business_type = st.selectbox("Business Type:",
                                    ['Restaurant/Cafe', 'Retail Shop', 'Gym/Fitness',
                                     'Education/Coaching', 'Healthcare/Clinic', 
                                     'Salon/Spa', 'Co-working Space', 'Other Service'])
        
        investment_budget = st.number_input("Total Investment Budget (₹ Lakhs):",
                                           min_value=5, max_value=100, value=20)
        
        monthly_budget = st.number_input("Monthly Operating Budget (₹):",
                                        min_value=10000, max_value=200000, 
                                        value=50000, step=5000)
    
    with col2:
        target_customers = st.multiselect("Target Customers:",
                                         ['Students', 'Office Workers', 'Families',
                                          'Senior Citizens', 'Tourists'],
                                         default=['Office Workers'])
        
        preferred_area = st.selectbox("Preferred Area Type:",
                                     ['Urban', 'Semi-Urban', 'Rural', 'Any'])
        
        priority = st.radio("Priority:",
                           ['High Footfall', 'Low Rent', 'Balanced'])
    
    if st.button("🎯 Get Recommendations", type="primary"):
        
        # Filter logic based on business type
        if preferred_area != 'Any':
            recommendations = df[df['area_type'] == preferred_area]
        else:
            recommendations = df.copy()
        
        recommendations = recommendations[
            recommendations['monthly_rent'] <= monthly_budget
        ]
        
        # Sort based on priority
        if priority == 'High Footfall':
            recommendations = recommendations.sort_values('footfall_score', ascending=False)
        elif priority == 'Low Rent':
            recommendations = recommendations.sort_values('monthly_rent', ascending=True)
        else:
            recommendations = recommendations.sort_values('economic_health_score', ascending=False)
        
        st.markdown("---")
        st.success(f"📍 Found {len(recommendations)} suitable locations!")
        
        # Display top 3 recommendations
        for i, (idx, row) in enumerate(recommendations.head(3).iterrows(), 1):
            with st.container():
                st.write(f"## Recommendation #{i}")
                
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("📍 Location", row['area_name'])
                    st.write(f"**City:** {row['city']}")
                
                with col2:
                    st.metric("💰 Monthly Rent", f"₹{row['monthly_rent']:,.0f}")
                    st.metric("📊 Health Score", f"{row['economic_health_score']:.1f}")
                
                with col3:
                    st.metric("👥 Footfall Score", f"{row['footfall_score']:.1f}/100")
                    st.metric("🏗️ Infrastructure", f"{row['infrastructure_score']:.1f}/100")
                
                with col4:
                    st.metric("📈 Growth", row['business_growth'])
                    st.metric("⚠️ Risk Score", f"{row['risk_score']:.1f}")
                
                st.write(f"**Why this location:** {row['recommended_business']}")
                
                # Calculate ROI estimate
                estimated_customers = row['avg_daily_customers'] * 0.8 # 80% capture
                estimated_revenue = estimated_customers * 30 * 500 # Assuming ₹500 avg transaction
                roi_months = (investment_budget * 100000) / (estimated_revenue - row['monthly_rent'])
                
                st.write(f"**Estimated Monthly Revenue:** ₹{estimated_revenue:,.0f}")
                st.write(f"**Estimated ROI Period:** {roi_months:.1f} months")
                
                st.markdown("---")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>🏙️ Hyperlocal Economy Intelligence System | Built with Streamlit & Python</p>
    <p>Data updated: 2025 | Analyzing 200+ locations across Punjab-Haryana</p>
</div>
""", unsafe_allow_html=True)
