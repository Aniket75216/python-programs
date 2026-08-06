// Home.tsx
import React from 'react';

const Home = () => {
    return (
        <div className="flex flex-col h-full p-4 bg-light-blue-50">
            <img src="logo.png" alt="Konkan Fish Market Logo" className="mx-auto" />
            <h1 className="text-xl font-bold text-center">Konkan Fish Market</h1>
            <input type="text" placeholder="Search fish, market or seller" className="p-2 mt-4 rounded border" />
            <div className="mt-4">
                <h2 className="text-lg font-semibold">Today's Fish Prices</h2>
                {/* Today's Fish Prices Section */}
                <div className="grid grid-cols-2 mt-2 gap-2">
                    {/* Price Cards */}
                </div>
            </div>
            <h2 className="text-lg font-semibold mt-4">Popular Fish</h2>
            <div className="flex overflow-x-scroll">
                {/* Horizontal scrolling card components */}
            </div>
            <h2 className="text-lg font-semibold mt-4">Fresh Catch Today</h2>
            {/* Fresh Catch Section */}
            <div className="flex flex-wrap justify-around mt-4">
                <button className="bg-blue-500 text-white rounded-full p-2">View Fish</button>
                <button className="bg-blue-500 text-white rounded-full p-2">Check Prices</button>
                <button className="bg-blue-500 text-white rounded-full p-2">Find Markets</button>
                <button className="bg-blue-500 text-white rounded-full p-2">Buy Fish</button>
            </div>
            {/* Bottom Navigation */}
            <nav className="fixed bottom-0 left-0 right-0">
                {/* Navigation Bar */}
            </nav>
        </div>
    );
};

export default Home;
